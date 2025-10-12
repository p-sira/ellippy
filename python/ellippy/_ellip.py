# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

from collections.abc import Callable
import numpy as np
from numpy.typing import ArrayLike, NDArray

from .ellippy_binding import (
    ellipk,
    ellipe,
    ellippi,
    ellipd,
    ellipf,
    ellipeinc,
    ellippiinc,
    ellipdinc,
    ellippiinc_bulirsch,
    cel,
    cel1,
    cel2,
    el1,
    el2,
    el3,
    elliprf,
    elliprg,
    elliprj,
    elliprc,
    elliprd,
    jacobi_zeta,
    heuman_lambda,
)

FloatArray = NDArray[np.float64]


def asarray(x: ArrayLike) -> FloatArray:
    return np.array(x, dtype=np.float64).flatten()


def returnfloat_single(func: Callable, arg: ArrayLike) -> FloatArray | float:
    try:
        ans = func(asarray(arg))
    except RuntimeError as e:
        raise ValueError(e)
    return ans.item() if isinstance(arg, float) else ans


def returnfloat(func: Callable, *args: ArrayLike) -> FloatArray | float:
    args_asarray = tuple(asarray(arg) for arg in args)
    try:
        ans = func(*args_asarray)
    except RuntimeError as e:
        raise ValueError(e)
    return ans.item() if isinstance(args[0], float) else ans
