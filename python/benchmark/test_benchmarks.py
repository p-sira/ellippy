# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

"""
Performance benchmarks for EllipPy, run with pytest-codspeed.

Each function is benchmarked twice:
- with scalar inputs, which goes through the scalar fast path,
- with numpy array inputs, which goes through the vectorized (rayon) path.

Run locally with:
    uv run pytest python/benchmark --codspeed
"""

import numpy as np
import pytest

import ellippy

ARRAY_SIZE = 1_000

_rng = np.random.default_rng(42)


def _uniform(low: float, high: float) -> np.ndarray:
    return _rng.uniform(low, high, ARRAY_SIZE)


# Inputs within the valid domain of every function.
_phi = _uniform(0.0, np.pi / 2)
_m = _uniform(0.0, 0.99)
_n = _uniform(0.0, 0.9)
_kc = _uniform(0.1, 1.0)
_p = _uniform(0.1, 2.0)
_a = _uniform(0.1, 2.0)
_b = _uniform(0.1, 2.0)
_x = _uniform(0.1, 5.0)
_xyz = [_uniform(0.1, 5.0) for _ in range(4)]

# (function name, scalar args, array args)
CASES = [
    # Legendre complete
    ("ellipk", (0.5,), (_m,)),
    ("ellipe", (0.5,), (_m,)),
    ("ellippi", (0.3, 0.5), (_n, _m)),
    ("ellipd", (0.5,), (_m,)),
    # Legendre incomplete
    ("ellipf", (0.8, 0.5), (_phi, _m)),
    ("ellipeinc", (0.8, 0.5), (_phi, _m)),
    ("ellippiinc", (0.8, 0.3, 0.5), (_phi, _n, _m)),
    ("ellippiinc_bulirsch", (0.8, 0.3, 0.5), (_phi, _n, _m)),
    ("ellipdinc", (0.8, 0.5), (_phi, _m)),
    # Bulirsch
    ("cel", (0.5, 1.2, 1.0, 0.7), (_kc, _p, _a, _b)),
    ("cel1", (0.5,), (_kc,)),
    ("cel2", (0.5, 1.0, 0.7), (_kc, _a, _b)),
    ("el1", (1.2, 0.5), (_x, _kc)),
    ("el2", (1.2, 0.5, 1.0, 0.7), (_x, _kc, _a, _b)),
    ("el3", (1.2, 0.5, 1.2), (_x, _kc, _p)),
    # Carlson
    ("elliprf", (1.0, 2.0, 3.0), tuple(_xyz[:3])),
    ("elliprg", (1.0, 2.0, 3.0), tuple(_xyz[:3])),
    ("elliprj", (1.0, 2.0, 3.0, 4.0), tuple(_xyz)),
    ("elliprc", (1.0, 2.0), tuple(_xyz[:2])),
    ("elliprd", (1.0, 2.0, 3.0), tuple(_xyz[:3])),
    # Misc
    ("jacobi_zeta", (0.8, 0.5), (_phi, _m)),
    ("heuman_lambda", (0.8, 0.5), (_phi, _m)),
]

_IDS = [name for name, _, _ in CASES]


@pytest.mark.parametrize("name,scalar_args,array_args", CASES, ids=_IDS)
def test_scalar(benchmark, name, scalar_args, array_args):
    func = getattr(ellippy, name)
    result = benchmark(func, *scalar_args)
    assert np.isfinite(result)


@pytest.mark.parametrize("name,scalar_args,array_args", CASES, ids=_IDS)
def test_array(benchmark, name, scalar_args, array_args):
    func = getattr(ellippy, name)
    result = benchmark(func, *array_args)
    assert result.shape == (ARRAY_SIZE,)
    assert np.all(np.isfinite(result))
