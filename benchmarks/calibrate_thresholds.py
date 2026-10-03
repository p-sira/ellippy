from __future__ import annotations

import json
import os
import time
from pathlib import Path

import numpy as np

import ellippy

ROOT = Path(__file__).resolve().parents[1]
OUT_PATH = ROOT / "vendor" / "ellip" / "ellip-rayon" / "benches" / "par_threshold.json"

FUNCTIONS_BY_ARGS = {
    1: ["ellipk", "ellipe", "ellipd", "cel1", "ellipke"],
    2: [
        "ellipf",
        "ellipeinc",
        "ellippi",
        "ellipdinc",
        "cel3",
        "el1",
        "elliprc",
        "jacobi_zeta",
        "heuman_lambda",
    ],
    3: [
        "ellippiinc",
        "ellippiinc_bulirsch",
        "cel2",
        "el3",
        "elliprf",
        "elliprg",
        "elliprd",
    ],
    4: ["cel", "el2", "elliprj"],
}


def measure_median_ns(fn, *args, force_par: bool, repeats: int = 11, warmup: int = 3) -> int:
    # Calibration hook: this is intentionally temporary and kept only for measuring
    # the real FFI crossover point. The final library uses the generated thresholds.
    os.environ["ELLIP_FORCE_PAR"] = "1" if force_par else "0"

    for _ in range(warmup):
        fn(*args)

    samples: list[int] = []
    for _ in range(repeats):
        t0 = time.perf_counter_ns()
        fn(*args)
        samples.append(time.perf_counter_ns() - t0)

    return int(np.median(samples))


def find_crossover(fn, arg_gen, low: int = 500, high: int = 50_000, tolerance: float = 0.03) -> int:
    best_crossover = high
    while low <= high:
        mid = (low + high) // 2
        args = arg_gen(mid)

        t_seq = measure_median_ns(fn, *args, force_par=False)
        t_par = measure_median_ns(fn, *args, force_par=True)
        ratio = t_par / max(t_seq, 1)

        if ratio < 1.0 - tolerance:
            best_crossover = mid
            high = mid - 100
        else:
            low = mid + 100

    return best_crossover


def calibrate_all() -> dict[str, int]:
    print("Calibrating FFI thresholds for all functions...\n")
    thresholds: dict[str, int] = {}

    for num_args, names in FUNCTIONS_BY_ARGS.items():
        for idx, name in enumerate(names):
            func = getattr(ellippy, name, None)
            if func is None:
                print(f"Skipping {name} (not found in ellippy module).")
                continue

            rng = np.random.default_rng(1337 + idx)

            def arg_gen(length: int, *, _nargs=num_args, _rng=rng):
                return tuple(_rng.uniform(0.1, 0.9, size=length) for _ in range(_nargs))

            print(f"Calibrating {name}...")
            threshold = find_crossover(func, arg_gen)
            thresholds[name] = threshold
            print(f"  -> {name} FFI threshold: {threshold}")

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(thresholds, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"\nSaved FFI-calibrated thresholds to {OUT_PATH}")
    return thresholds


if __name__ == "__main__":
    calibrate_all()
