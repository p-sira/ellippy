#!/usr/bin/env python3
# EllipPy is licensed under The 3-Clause BSD; see LICENSE.
"""Measure full public-Python calls with isolated Rayon and GIL policies."""

from __future__ import annotations

import argparse
import gc
import hashlib
import itertools
import json
import math
import os
import platform
import random
import statistics
import subprocess
import sys
import threading
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
# Valid, varied arguments: conversion is repeated in the timed public call.
ARGS = {
    "ellipk": "m",
    "ellipe": "m",
    "ellipke": "m",
    "ellipd": "m",
    "ellipf": "phi m",
    "ellipeinc": "phi m",
    "ellipdinc": "phi m",
    "ellippi": "n m",
    "ellippiinc": "phi n m",
    "ellippiinc_bulirsch": "phi n m",
    "cel": "kc p a b",
    "cel1": "kc",
    "cel2": "kc a b",
    "cel3": "kc p",
    "el1": "x kc",
    "el2": "x kc a b",
    "el3": "x kc p",
    "elliprf": "x y z",
    "elliprg": "x y z",
    "elliprj": "x y z p",
    "elliprc": "x y",
    "elliprd": "x y z",
    "jacobi_zeta": "phi m",
    "heuman_lambda": "phi m",
}
LAYOUTS = ("contiguous_f64", "contiguous_f32", "strided_f64", "python_list")
DISTRIBUTIONS = ("uniform", "near_boundary")
POLICIES = (
    "serial:retain",
    "parallel:retain",
    "serial:detach",
    "parallel:detach",
    "auto:retain",
    "auto:detach",
    "auto:auto",
)
COMPARISONS = {
    "rayon": ("serial:retain", "parallel:retain"),
    "rayon_detached": ("serial:detach", "parallel:detach"),
    "gil": ("auto:retain", "auto:detach"),
}


def fixture(case, size, layout, distribution):
    import numpy as np

    # Stable across processes, policies and layouts.
    seed = int.from_bytes(
        hashlib.sha256(f"{case}:{size}:{distribution}".encode()).digest()[:4], "little"
    )
    rng = np.random.default_rng(seed)
    limits = {
        "m": (0.0, 0.99),
        "n": (0.0, 0.9),
        "phi": (0.05, 1.5),
        "kc": (0.1, 1.0),
        "p": (0.1, 2.0),
        "a": (0.1, 2.0),
        "b": (0.1, 2.0),
        "x": (0.1, 5.0),
        "y": (0.1, 5.0),
        "z": (0.1, 5.0),
    }
    if distribution == "near_boundary":
        limits.update(
            m=(0.99, 0.9999), n=(0.98, 0.999), kc=(0.01, 0.05), phi=(1.5, 1.56)
        )
    args = []
    for name in ARGS[case].split():
        values = rng.uniform(*limits[name], size)
        if layout == "contiguous_f32":
            values = values.astype(np.float32)
        elif layout == "strided_f64":
            storage = np.empty(size * 2)
            storage[::2] = values
            values = storage[::2]
        elif layout == "python_list":
            values = values.tolist()
        args.append(values)
    return args


def verify_counts(state, rust, gil, size, thresholds):
    parallel = rust == "parallel" or (rust == "auto" and size >= thresholds[0])
    detach = gil == "detach" or (gil == "auto" and size >= thresholds[1])
    expected = {
        "rust_branches": [int(not parallel), int(parallel)],
        "gil_branches": [int(not detach), int(detach)],
    }
    for key, counts in expected.items():
        if list(state[key]) != counts:
            raise RuntimeError(f"wrong {key}: {state[key]} != {counts}")


def measure_task(binding, task, request):
    import ellippy
    import numpy as np

    case, size, _layout, _distribution = task
    args = fixture(*task)
    fn = getattr(ellippy, case)
    call = lambda: fn(*args)
    rust, gil = request["policy"].split(":")
    binding._set_threshold_calibration("serial", "retain", True)
    reference = call()
    binding._set_threshold_calibration(rust, gil, True)
    actual = call()
    state = binding._threshold_calibration_state()
    verify_counts(state, rust, gil, size, state["thresholds"][case])
    # Compare tuple members separately, including empty arrays.
    for lhs, rhs in zip(
        reference if isinstance(reference, tuple) else (reference,),
        actual if isinstance(actual, tuple) else (actual,),
    ):
        np.testing.assert_allclose(lhs, rhs, rtol=1e-13, atol=1e-14, equal_nan=True)
    binding._set_threshold_calibration(rust, gil, False)
    for _ in range(request["warmups"]):
        call()
    start = time.perf_counter_ns()
    call()
    estimate = max(1, time.perf_counter_ns() - start)
    loops = max(
        1, min(request["max_loops"], int(request["target_sample_ms"] * 1e6 / estimate))
    )
    samples = []
    enabled = gc.isenabled()
    gc.disable()
    try:
        for _ in range(request["repeats"]):
            start = time.perf_counter_ns()
            for _ in range(loops):
                call()
            samples.append((time.perf_counter_ns() - start) / loops)
    finally:
        if enabled:
            gc.enable()
    return {
        "task": task,
        "policy": request["policy"],
        "round": request["round"],
        "phase": request["phase"],
        "loops": loops,
        "samples_ns": samples,
        "verification": {key: state[key] for key in ("rust_branches", "gil_branches")},
    }


def responsiveness(binding, case, size, policy, repeats):
    """Measure background-thread progress separately from latency samples."""
    import ellippy

    fn = getattr(ellippy, case)
    args = fixture(case, size, "contiguous_f64", "uniform")
    rust, gil = policy.split(":")
    binding._set_threshold_calibration(rust, gil, False)
    results = []
    for _ in range(repeats):
        stop = threading.Event()
        ready = threading.Event()
        ticks = []

        def probe(ready=ready, stop=stop, ticks=ticks):
            ready.set()
            while not stop.wait(0.0005):
                ticks.append(time.perf_counter_ns())

        thread = threading.Thread(target=probe)
        thread.start()
        ready.wait()
        try:
            start = time.perf_counter_ns()
            fn(*args)
            end = time.perf_counter_ns()
        finally:
            stop.set()
            thread.join()
        results.append(
            {
                "duration_ns": end - start,
                "ticks_during_call": sum(start <= t <= end for t in ticks),
            }
        )
    return {"case": case, "size": size, "policy": policy, "samples": results}


def worker(request):
    import ellippy.ellippy_binding as binding
    import numpy as np

    if not hasattr(binding, "_set_threshold_calibration"):
        raise RuntimeError(
            "Rebuild with uv run maturin develop --release --features threshold-calibration"
        )
    state = binding._threshold_calibration_state()
    extension = Path(binding.__file__).resolve()
    tasks = list(request["tasks"])
    random.Random(request["seed"] + request["round"]).shuffle(tasks)
    records = [measure_task(binding, task, request) for task in tasks]
    probes = [
        responsiveness(binding, case, size, request["policy"], request["repeats"])
        for case, size in request.get("probes", [])
    ]
    return {
        "records": records,
        "responsiveness": probes,
        "provenance": {
            "python": sys.version,
            "numpy": np.__version__,
            "extension": str(extension),
            "extension_sha256": hashlib.sha256(extension.read_bytes()).hexdigest(),
            "gil_enabled": getattr(sys, "_is_gil_enabled", lambda: True)(),
            "rayon_threads": state["rayon_threads"],
            "thresholds": state["thresholds"],
        },
    }


def candidates(records):
    grouped = {}
    for record in records:
        case, size, layout, distribution = record["task"]
        key = (case, layout, distribution)
        grouped.setdefault(key, {}).setdefault(size, {}).setdefault(
            record["policy"], {}
        )[record["round"]] = statistics.median(record["samples_ns"])
    output = []
    for (case, layout, distribution), by_size in sorted(grouped.items()):
        for comparison, (left, right) in COMPARISONS.items():
            points = []
            for size, policies in sorted(by_size.items()):
                if size == 0 or left not in policies or right not in policies:
                    continue
                rounds = sorted(set(policies[left]) & set(policies[right]))
                ratios = [policies[right][r] / policies[left][r] for r in rounds]
                qualifies = statistics.median(ratios) <= 0.95 and sum(
                    r <= 0.95 for r in ratios
                ) >= math.ceil(2 * len(ratios) / 3)
                points.append(
                    {
                        "size": size,
                        "ratio": statistics.median(ratios),
                        "qualifies": qualifies,
                        "round_ratios": ratios,
                    }
                )
            # Require an adjacent pair and no later reversal on this tested grid.
            index = next(
                (
                    i
                    for i in range(len(points) - 1)
                    if all(p["qualifies"] for p in points[i:])
                ),
                None,
            )
            confirmed = index is not None
            first = points[index]["size"] if confirmed else None
            lower = points[index - 1]["size"] if confirmed and index > 0 else 0
            output.append(
                {
                    "case": case,
                    "layout": layout,
                    "distribution": distribution,
                    "comparison": comparison,
                    "status": "crossover"
                    if confirmed
                    else "inconclusive"
                    if any(p["qualifies"] for p in points)
                    else "no_crossover",
                    "first_switch_size": first,
                    "candidate_range": [lower + 1, first] if confirmed else None,
                    "maximum_tested_size": max(by_size),
                    "points": points,
                }
            )
    return output


def run_worker(request):
    completed = subprocess.run(
        [sys.executable, str(Path(__file__).resolve()), "--worker"],
        input=json.dumps(request),
        text=True,
        capture_output=True,
        check=False,
        cwd=ROOT,
    )
    if completed.returncode:
        raise RuntimeError(completed.stderr.strip() or "calibration worker failed")
    return json.loads(completed.stdout)


def git(*args):
    return subprocess.run(
        ["git", "-C", str(ROOT), *args], capture_output=True, text=True, check=True
    ).stdout.strip()


def run(args):
    tasks = list(
        itertools.product(
            args.cases, args.sizes, ["contiguous_f64"], args.distributions
        )
    )
    if args.preflight:
        tasks = list(
            itertools.product(args.cases, [0, 1, 33], LAYOUTS, args.distributions)
        )
    if args.validate_defaults:
        built = run_worker(
            {"tasks": [], "policy": "auto:auto", "round": 0, "seed": args.seed}
        )
        tasks = sorted(
            {
                (case, size, layout, distribution)
                for case in args.cases
                for threshold in built["provenance"]["thresholds"][case]
                if threshold <= args.max_size
                for size in (
                    max(1, threshold - 1),
                    threshold,
                    min(2 * threshold, args.max_size),
                )
                for layout in LAYOUTS
                for distribution in args.distributions
            }
        )
        if not tasks:
            raise SystemExit("No compiled cutovers within --max-size")
    if args.dry_run:
        print(
            json.dumps(
                {
                    "coarse_tasks": len(tasks),
                    "policies": POLICIES,
                    "rounds": args.policy_rounds,
                    "max_size": args.max_size,
                    "validation_layouts": args.validation_layouts,
                },
                indent=2,
            )
        )
        return
    stamp = time.strftime("%Y%m%d-%H%M%S")
    directory = args.results_dir / f"python-path-{stamp}-{os.getpid()}"
    if not args.preflight:
        directory.mkdir(parents=True)
    report = {
        "schema": 1,
        "provenance": {
            "platform": platform.platform(),
            "cpu_count": os.cpu_count(),
            "affinity": sorted(os.sched_getaffinity(0))
            if hasattr(os, "sched_getaffinity")
            else None,
            "rayon_num_threads": os.environ.get("RAYON_NUM_THREADS"),
            "revision": git("rev-parse", "HEAD"),
            "git_status": git("status", "--porcelain"),
            "command": sys.argv,
            "source_sha256": {
                str(p.relative_to(ROOT)): hashlib.sha256(p.read_bytes()).hexdigest()
                for p in sorted((ROOT / "src").glob("*.rs"))
                + [ROOT / "Cargo.lock", Path(__file__)]
            },
        },
        "configuration": {
            key: str(value) if isinstance(value, Path) else value
            for key, value in vars(args).items()
        },
        "workers": [],
        "records": [],
        "responsiveness": [],
        "candidates": [],
    }

    def save_report():
        target = directory / "report.json"
        temporary = target.with_suffix(".tmp")
        temporary.write_text(json.dumps(report, indent=2) + "\n")
        temporary.replace(target)

    def sweep(tasks, phase):
        for round_number in range(1 if args.preflight else args.policy_rounds):
            policies = list(POLICIES)
            shift = round_number % len(policies)
            policies = policies[shift:] + policies[:shift]
            if round_number % 2:
                policies.reverse()
            for policy in policies:
                print(
                    f"{phase}: round {round_number + 1}, {policy}, {len(tasks)} calls",
                    file=sys.stderr,
                    flush=True,
                )
                request = {
                    "tasks": tasks,
                    "policy": policy,
                    "round": round_number,
                    "phase": phase,
                    "seed": args.seed,
                    "repeats": 1 if args.preflight else args.repeats,
                    "warmups": args.warmups,
                    "max_loops": 1 if args.preflight else args.max_loops,
                    "target_sample_ms": args.target_sample_ms,
                }
                result = run_worker(request)
                if (
                    report["workers"]
                    and result["provenance"] != report["workers"][0]["provenance"]
                ):
                    raise RuntimeError("Build or environment changed between workers")
                report["workers"].append(
                    {
                        "policy": policy,
                        "round": round_number,
                        "phase": phase,
                        "provenance": result["provenance"],
                    }
                )
                report["records"].extend(result["records"])
                if not args.preflight:
                    save_report()

    sweep(
        tasks,
        "preflight"
        if args.preflight
        else "default-validation"
        if args.validate_defaults
        else "coarse",
    )
    if args.preflight:
        print(f"Preflight passed: {len(tasks)} workloads × {len(POLICIES)} policies")
        return
    if not args.validate_defaults:
        # Extend unresolved workloads, then refine each detected transition.
        for _step in range(args.extension_steps):
            summary = candidates(report["records"])
            unresolved = {
                (r["case"], r["distribution"])
                for r in summary
                if r["status"] != "crossover"
            }
            next_size = min(max(t[1] for t in tasks) * 2, args.max_size)
            if not unresolved or next_size <= max(t[1] for t in tasks):
                break
            extra = [
                (case, next_size, "contiguous_f64", dist)
                for case, dist in sorted(unresolved)
            ]
            sweep(extra, "extension")
            tasks.extend(extra)
        summary = candidates(report["records"])
        extra = set()
        for row in summary:
            if row["status"] == "crossover":
                low, high = row["candidate_range"]
                for i in range(1, args.refinement_points + 1):
                    size = round(low + (high - low) * i / (args.refinement_points + 1))
                    extra.add(
                        (row["case"], size, "contiguous_f64", row["distribution"])
                    )
        extra -= set(tasks)
        if extra:
            sweep(sorted(extra), "refinement")
        summary = candidates(report["records"])
        validation = set()
        for row in summary:
            if row["status"] == "crossover":
                # Include the next tested size so validation has adjacent evidence.
                sizes = [p["size"] for p in row["points"]]
                first = row["first_switch_size"]
                for size in (max(1, first - 1), first, sizes[sizes.index(first) + 1]):
                    for layout in args.validation_layouts:
                        validation.add((row["case"], size, layout, row["distribution"]))
        if validation:
            sweep(sorted(validation), "layout-validation")
    if args.responsiveness:
        for policy in ("auto:retain", "auto:detach"):
            request = {
                "tasks": [],
                "probes": [(case, args.max_size) for case in args.cases],
                "policy": policy,
                "round": 0,
                "seed": args.seed,
                "repeats": args.repeats,
            }
            report["responsiveness"].extend(run_worker(request)["responsiveness"])
    report["candidates"] = candidates(report["records"])
    save_report()
    print(directory / "report.json")


def csv(value):
    return [part.strip() for part in value.split(",") if part.strip()]


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--worker", action="store_true", help=argparse.SUPPRESS)
    p.add_argument("--cases", type=csv, default=list(ARGS))
    p.add_argument(
        "--sizes",
        type=lambda v: [int(x) for x in csv(v)],
        default=[0, 1, 8, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192],
    )
    p.add_argument("--distributions", type=csv, default=list(DISTRIBUTIONS))
    p.add_argument("--validation-layouts", type=csv, default=list(LAYOUTS[1:]))
    p.add_argument("--results-dir", type=Path, default=ROOT / "benchmark-results")
    p.add_argument("--repeats", type=int, default=5)
    p.add_argument("--warmups", type=int, default=3)
    p.add_argument("--target-sample-ms", type=float, default=5.0)
    p.add_argument("--max-loops", type=int, default=100_000)
    p.add_argument("--policy-rounds", type=int, default=3)
    p.add_argument("--seed", type=int, default=20261014)
    p.add_argument("--extension-steps", type=int, default=3)
    p.add_argument("--max-size", type=int, default=65536)
    p.add_argument("--refinement-points", type=int, default=3)
    p.add_argument(
        "--responsiveness", action=argparse.BooleanOptionalAction, default=True
    )
    mode = p.add_mutually_exclusive_group()
    mode.add_argument("--preflight", action="store_true")
    mode.add_argument(
        "--validate-defaults",
        action="store_true",
        help="verify compiled cutovers and their neighbors across all layouts",
    )
    p.add_argument("--dry-run", action="store_true")
    return p


def main():
    args = parser().parse_args()
    if args.worker:
        print(json.dumps(worker(json.load(sys.stdin))))
        return
    if not args.cases or set(args.cases) - ARGS.keys():
        raise SystemExit("--cases must contain known function names")
    if not args.distributions or set(args.distributions) - set(DISTRIBUTIONS):
        raise SystemExit("Unknown or empty --distributions")
    if set(args.validation_layouts) - set(LAYOUTS):
        raise SystemExit("Unknown --validation-layouts")
    if (
        not args.sizes
        or min(args.sizes) < 0
        or max(args.sizes) > args.max_size
        or len(set(args.sizes)) < 2
    ):
        raise SystemExit("Need at least two non-negative sizes, at most --max-size")
    if (
        min(args.repeats, args.policy_rounds, args.max_loops, args.max_size) < 1
        or min(args.warmups, args.extension_steps, args.refinement_points) < 0
        or not math.isfinite(args.target_sample_ms)
        or args.target_sample_ms <= 0
    ):
        raise SystemExit("Invalid measurement limits")
    args.sizes = sorted(set(args.sizes))
    run(args)


if __name__ == "__main__":
    main()
