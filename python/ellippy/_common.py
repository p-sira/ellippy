# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

from collections.abc import Callable

import numpy as np
from numpy.typing import ArrayLike, NDArray

from . import ellippy_binding

FloatArray = NDArray[np.float64]

_SCALAR_FUNCS: dict[Callable, Callable] = {}
for _name in [
    "ellipk", "ellipe", "ellipf", "ellipeinc", "ellippi", "ellippiinc",
    "ellippiinc_bulirsch", "ellipd", "ellipdinc", "cel", "cel1", "cel2",
    "el1", "el2", "el3", "elliprf", "elliprg", "elliprj", "elliprc",
    "elliprd", "jacobi_zeta", "heuman_lambda",
]:
    _arr_fn = getattr(ellippy_binding, _name, None)
    _scalar_fn = getattr(ellippy_binding, f"{_name}_scalar", None)
    if _arr_fn is not None and _scalar_fn is not None:
        _SCALAR_FUNCS[_arr_fn] = _scalar_fn


_SCALAR_TYPES = (float, int, np.floating, np.integer)


def _is_scalar(x: object) -> bool:
    return isinstance(x, _SCALAR_TYPES) or (isinstance(x, np.ndarray) and x.ndim == 0)


def asarray(x: ArrayLike) -> FloatArray:
    return np.ascontiguousarray(x, dtype=np.float64).ravel()


def returnfloat_single(func: Callable, arg: ArrayLike) -> FloatArray | float:
    if _is_scalar(arg):
        scalar_fn = _SCALAR_FUNCS.get(func)
        if scalar_fn is not None:
            try:
                return scalar_fn(float(arg))
            except RuntimeError as e:
                raise ValueError(e) from None
    try:
        ans = func(asarray(arg))
    except RuntimeError as e:
        raise ValueError(e) from None
    return ans.item() if _is_scalar(arg) else ans


def returnfloat(func: Callable, *args: ArrayLike) -> FloatArray | float:
    if all(_is_scalar(arg) for arg in args):
        scalar_fn = _SCALAR_FUNCS.get(func)
        if scalar_fn is not None:
            try:
                return scalar_fn(*(float(arg) for arg in args))
            except RuntimeError as e:
                raise ValueError(e) from None
    args_asarray = tuple(asarray(arg) for arg in args)
    try:
        ans = func(*args_asarray)
    except RuntimeError as e:
        raise ValueError(e) from None
    return ans.item() if _is_scalar(args[0]) else ans
