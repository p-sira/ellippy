# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

"""
Miscellaneous functions related to elliptic integrals.
"""

from numpy.typing import ArrayLike
from . import _ellip
from ._ellip import FloatArray, returnfloat


def jacobi_zeta(phi: ArrayLike, m: ArrayLike) -> FloatArray | float:
    r"""Computes Jacobi Zeta function Z(φ | m).

    .. math::

        Z(\varphi, m) = E(\varphi, m) - \frac{E(m)\,F(\varphi, m)}{K(m)}

    Args:
        phi (ArrayLike): Amplitude angle (φ) in radians. φ ∈ ℝ. 
        m (ArrayLike): Elliptic parameter. m ∈ ℝ, m ≤ 1.

    Returns:
        Scalar or `numpy.ndarray` broadcast from inputs.

    Raises:
        ValueError: If any m > 1, or phi/m are infinite, or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/jacobi_zeta.html" width="100%" height="500px"></iframe>

    Special Cases:
        - Z(0, m) = 0
        - Z(φ, 0) = 0
        - Z(φ, 1) = sin(φ)·sign(cos(φ)) for φ ≠ nπ/2
        - Z(nπ/2, m) = 0 for n ∈ ℤ
        - Z(φ, m) = -Z(−φ, m)

    Related Functions:
        - Z(φ, m) = E(φ, m) - E(m) F(φ, m) / K(m)
        - Z(φ, m) = m sin(φ) cos(φ) √(1 - m sin²φ) · RJ(0, k_c², 1, 1 - m sin²φ) / (3 K(m))

    References:
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed August 30, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Reinhardt, W. P., and P. L. Walker. “DLMF: Chapter 22 Jacobian Elliptic Functions.” Accessed August 31, 2025. https://dlmf.nist.gov/22.
        - Weisstein, Eric W. “Jacobi Zeta Function.” Wolfram Research, Inc. Accessed August 31, 2025. https://mathworld.wolfram.com/JacobiZetaFunction.html.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.jacobi_zeta, phi, m)


def heuman_lambda(phi: ArrayLike, m: ArrayLike) -> FloatArray | float:
    r"""Computes Heuman Lambda function Λ₀(φ | m).

    .. math::

        \Lambda_0(\varphi, m) = \frac{F\!\left(\varphi, 1-m\right)}{K\!\left(1-m\right)} + \frac{2}{\pi} K(m)\, Z\!\left(\varphi, 1-m\right)

    Args:
        phi (ArrayLike): Amplitude angle (φ) in radians. φ ∈ ℝ. 
        m (ArrayLike): Elliptic parameter. m ∈ ℝ, 0 ≤ m < 1.

    Returns:
        Scalar or `numpy.ndarray` broadcast from inputs.

    Raises:
        ValueError: If m < 0 or m ≥ 1, phi is infinite, or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/heuman_lambda.html" width="100%" height="500px"></iframe>

    Special Cases:
        - Λ₀(nπ/2, m) = n where n ∈ ℤ
        - Λ0(φ, 0) = sin(φ)

    Related Functions:
        With mc = 1 - m and Δ² = 1 - mc sin²φ:
            - Λ₀(φ, m) = F(φ, mc)/K(mc) + (2/π) K(m) Z(φ, mc)
            - Λ₀(φ, m) = 2/π · mc sin(φ) cos(φ)/Δ · [RF(0, mc, 1) + m/(3Δ²) RJ(0, mc, 1, 1 - m/Δ²)]

    References:
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed August 30, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.heuman_lambda, phi, m)
