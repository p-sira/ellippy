"""Verify policy controls against public API results, rather than timing noise."""

import importlib.util
from pathlib import Path

import ellippy as ep
import numpy as np
import pytest
from ellippy import ellippy_binding as binding

path = (
    Path(__file__).resolve().parents[2]
    / "benchmarks/perf_calibration/calibrate_thresholds.py"
)
spec = importlib.util.spec_from_file_location("calibration", path)
calibration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(calibration)

CALIBRATION = hasattr(binding, "_set_threshold_calibration")


@pytest.fixture(autouse=True)
def reset_policy():
    yield
    if CALIBRATION:
        binding._set_threshold_calibration()


@pytest.mark.skipif(not CALIBRATION, reason="requires threshold-calibration build")
@pytest.mark.parametrize("case", calibration.ARGS)
@pytest.mark.parametrize("policy", calibration.POLICIES)
def test_forced_policies(case, policy):
    for size in (0, 1, 65):
        calibration.measure_task(
            binding,
            (case, size, "strided_f64", "uniform"),
            {
                "policy": policy,
                "round": 0,
                "phase": "test",
                "warmups": 0,
                "max_loops": 1,
                "target_sample_ms": 1,
                "repeats": 1,
            },
        )


@pytest.mark.skipif(not CALIBRATION, reason="requires threshold-calibration build")
def test_controls_validate_atomically_and_counters_can_be_disabled():
    binding._set_threshold_calibration("serial", "retain", True)
    before = binding._threshold_calibration_state()
    with pytest.raises(ValueError):
        binding._set_threshold_calibration("parallel", "invalid")
    assert binding._threshold_calibration_state() == before
    with pytest.raises(ValueError):
        binding._set_threshold_calibration("invalid", "detach")
    binding._set_threshold_calibration("parallel", "detach", False)
    ep.ellipk([0.2, 0.3])
    state = binding._threshold_calibration_state()
    assert state["rust_branches"] == (0, 0)
    assert state["gil_branches"] == (0, 0)


def test_binding_rejects_noncontiguous_and_mismatched_arrays():
    with pytest.raises(ValueError, match="contiguous"):
        binding.ellipk(np.arange(6.0)[::2])
    with pytest.raises(ValueError, match="same length"):
        ep.ellipf([0.1, 0.2], [0.3])


def test_candidate_requires_stable_adjacent_evidence():
    def records(ratios):
        return [
            {
                "task": ("ellipk", 2**size, "contiguous_f64", "uniform"),
                "policy": policy,
                "round": round_number,
                "samples_ns": [100 if policy == "serial:retain" else 100 * ratio],
            }
            for size, ratio in enumerate(ratios)
            for policy in ("serial:retain", "parallel:retain")
            for round_number in range(3)
        ]

    def candidate(ratios):
        return calibration.candidates(records(ratios))[0]

    assert candidate([1, 0.9])["status"] == "inconclusive"
    assert candidate([1, 0.9, 0.9])["first_switch_size"] == 2
    assert candidate([1, 0.9, 0.9, 1])["status"] == "inconclusive"
    assert candidate([1, 1, 1])["status"] == "no_crossover"


@pytest.mark.skipif(not CALIBRATION, reason="requires threshold-calibration build")
@pytest.mark.parametrize("policy", calibration.POLICIES)
def test_domain_errors_under_each_policy(policy):
    binding._set_threshold_calibration(*policy.split(":"))
    with pytest.raises(ValueError):
        ep.ellipk([0.2, 2.0])
    with pytest.raises(ValueError):
        ep.ellipke([0.2, 2.0])


@pytest.mark.skipif(not CALIBRATION, reason="requires threshold-calibration build")
@pytest.mark.parametrize("case", calibration.ARGS)
def test_automatic_cutover_boundaries(case):
    state = binding._threshold_calibration_state()
    thresholds = state["thresholds"][case]
    sizes = {
        size
        for threshold in thresholds
        if threshold <= 65536
        for size in (max(0, threshold - 1), threshold)
    }
    for size in sizes:
        calibration.measure_task(
            binding,
            (case, size, "contiguous_f64", "uniform"),
            {
                "policy": "auto:auto",
                "round": 0,
                "phase": "test",
                "warmups": 0,
                "max_loops": 1,
                "target_sample_ms": 1,
                "repeats": 1,
            },
        )
