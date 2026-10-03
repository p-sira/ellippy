# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

from numpy.typing import ArrayLike
from . import _ellip
from ._ellip import FloatArray, returnfloat, returnfloat_single


def ellipk(m: ArrayLike) -> FloatArray | float:
    """Complete elliptic integral of the first kind K(m).

    Computes K(m) = ∫[0, π/2] dθ / sqrt(1 - m sin²θ).

    Args:
        m: Elliptic parameter. Real-valued array-like with m ≤ 1 allowed; m = 1 yields +∞, m = -∞ yields 0.

    Returns:
        Scalar or `numpy.ndarray` with the same shape as `m`.

    Raises:
        ValueError: If any m > 1 or inputs contain NaN.

    Notes:
        The elliptic modulus k is related by k² = m.

    References:
        - DLMF §19.2.8 (Complete elliptic integrals).
        - Rust crate `ellip` function `ellipk` docs.
    """
    return returnfloat_single(_ellip.ellipk, m)


def ellipe(m: ArrayLike) -> FloatArray | float:
    """Complete elliptic integral of the second kind E(m).

    Computes E(m) = ∫[0, π/2] sqrt(1 - m sin²θ) dθ.

    Args:
        m: Elliptic parameter. Real-valued array-like with m ≤ 1 allowed; E(1) = 1, E(-∞) = ∞.

    Returns:
        Scalar or `numpy.ndarray` with the same shape as `m`.

    Raises:
        ValueError: If any m > 1 or inputs contain NaN.

    References:
        - DLMF §19.2.8; Rust crate `ellip` function `ellipe`.
    """
    return returnfloat_single(_ellip.ellipe, m)


def ellippi(n: ArrayLike, m: ArrayLike) -> FloatArray | float:
    """Complete elliptic integral of the third kind Π(n | m).

    Args:
        n: Characteristic parameter. Real-valued array-like.
        m: Elliptic parameter. Real-valued array-like.

    Returns:
        Scalar or `numpy.ndarray` broadcast from `n` and `m`.

    Raises:
        ValueError: On domain errors or NaNs.
    """
    return returnfloat(_ellip.ellippi, n, m)


def ellipd(m: ArrayLike) -> FloatArray | float:
    """Complete elliptic integral of Legendre's type D(m).

    Args:
        m: Elliptic parameter. Real-valued array-like.

    Returns:
        Scalar or `numpy.ndarray` with the same shape as `m`.
    """
    return returnfloat_single(_ellip.ellipd, m)


def ellipf(phi: ArrayLike, m: ArrayLike) -> FloatArray | float:
    """Incomplete elliptic integral of the first kind F(φ | m).

    Args:
        phi: Amplitude φ (radians). Real-valued array-like.
        m: Elliptic parameter. Real-valued array-like.

    Returns:
        Scalar or `numpy.ndarray` broadcast from `phi` and `m`.
    """
    return returnfloat(_ellip.ellipf, phi, m)


def ellipeinc(phi: ArrayLike, m: ArrayLike) -> FloatArray | float:
    """Incomplete elliptic integral of the second kind E(φ | m).

    Args:
        phi: Amplitude φ (radians). Real-valued array-like.
        m: Elliptic parameter. Real-valued array-like.

    Returns:
        Scalar or `numpy.ndarray` broadcast from `phi` and `m`.
    """
    return returnfloat(_ellip.ellipeinc, phi, m)


def ellippiinc(n: ArrayLike, phi: ArrayLike, m: ArrayLike) -> FloatArray | float:
    """Incomplete elliptic integral of the third kind Π(n; φ | m).

    Args:
        n: Characteristic parameter. Real-valued array-like.
        phi: Amplitude φ (radians). Real-valued array-like.
        m: Elliptic parameter. Real-valued array-like.

    Returns:
        Scalar or `numpy.ndarray` broadcast from `n`, `phi`, and `m`.
    """
    return returnfloat(_ellip.ellippiinc, n, phi, m)


def ellipdinc(phi: ArrayLike, m: ArrayLike) -> FloatArray | float:
    """Incomplete elliptic integral of Legendre's type D(φ | m).

    Args:
        phi: Amplitude φ (radians). Real-valued array-like.
        m: Elliptic parameter. Real-valued array-like.

    Returns:
        Scalar or `numpy.ndarray` broadcast from `phi` and `m`.
    """
    return returnfloat(_ellip.ellipdinc, phi, m)


def ellippiinc_bulirsch(
    n: ArrayLike, phi: ArrayLike, m: ArrayLike
) -> FloatArray | float:
    """Incomplete Π(n; φ | m) using Bulirsch's faster formulation.

    Same value as `ellippiinc` but uses a faster algorithm for many inputs.

    Args:
        n: Characteristic parameter. Real-valued array-like.
        phi: Amplitude φ (radians). Real-valued array-like.
        m: Elliptic parameter. Real-valued array-like.

    Returns:
        Scalar or `numpy.ndarray` broadcast from `n`, `phi`, and `m`.
    """
    return returnfloat(_ellip.ellippiinc_bulirsch, n, phi, m)
