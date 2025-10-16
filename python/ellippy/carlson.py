# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

"""
Elliptic integral functions in Carlson's form.
"""

from numpy.typing import ArrayLike
from . import _ellip
from ._ellip import FloatArray, returnfloat


def elliprf(x: ArrayLike, y: ArrayLike, z: ArrayLike) -> FloatArray | float:
    r"""Computes Carlson symmetric integral RF.

    .. math::

        R_F(x, y, z) = \tfrac{1}{2} \int_0^{\infty} \frac{\mathrm{d}t}{\sqrt{(t+x)(t+y)(t+z)}}

    Args:
        x, y, z (ArrayLike): Real-valued parameter.

    Returns:
        Scalar or `numpy.ndarray` broadcast from inputs.

    Raises:
        ValueError: If any of x, y, or z is negative, or more than one of them are zero, or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/elliprf.html" width="100%" height="500px"></iframe>

    Special Cases:
        - RF(x, x, x) = 1/sqrt(x)
        - RF(x, y, y) = RC(x, y)
        - RF(0, y, y) = π/(2 sqrt(y))
        - RF(x, y, z) = 0 for x = ∞ or y = ∞ or z = ∞

    Related Functions:
        With c = csc²φ, r = 1/x², and kc² = 1 - m,
        - F(φ,m) = RF(c - 1, c - m, c)
        - el1(x, kc) = RF(r, r + m, r + 1)

    Notes:
        The parameters x, y, and z are symmetric. This means swapping them does not change the 
        value of the function. At most one of them can be zero.
    
    References:
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.elliprf, x, y, z)


def elliprg(x: ArrayLike, y: ArrayLike, z: ArrayLike) -> FloatArray | float:
    r"""Computes Carlson symmetric integral RG.

    .. math::

        R_G(x,y,z) = \frac{1}{4}\int_{0}^{\infty}\frac{t}
            {\sqrt{(t+x)(t+y)(t+z)}}\,\left(\dfrac{x}{t+x}+\dfrac{y}{t+y}+\dfrac{z}{t+z}\right)\,\mathrm{d}t
    Args:
        x, y, z (ArrayLike): Real-valued parameter.

    Returns:
        Scalar or `numpy.ndarray` broadcast from inputs.
    
    Raises:
        ValueError: If any of x, y, or z is negative or infinite, or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/elliprg.html" width="100%" height="500px"></iframe>
    
    Special Cases:
        - RG(x, x, x) = sqrt(x)
        - RG(0, y, y) = π/4 * sqrt(y)
        - RG(x, y, y) = (y * RC(x, y) + sqrt(x))/2
        - RG(0, 0, z) = sqrt(z)/2

    Related Functions:
        With c = csc²φ, r = 1/x², and kc² = 1 - m,
            - E(m) = 2·RG(0, kc², 1)
            - 5(φ, m) = 2·RG(c - 1, c - m, c) - (c - 1)·RF(c - 1, c - m, c) - sqrt((c - 1) * (c - m) / c)

    Notes:
        The parameters x, y, and z are symmetric. This means swapping them does not change the 
        value of the function. At most one of them can be zero.
    
    References:
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.elliprg, x, y, z)


def elliprj(
    x: ArrayLike, y: ArrayLike, z: ArrayLike, p: ArrayLike
) -> FloatArray | float:
    r"""Computes Carlson symmetric integral RJ.

    .. math::

        R_J(x, y, z, p) = \tfrac{3}{2} \int_0^{\infty} \frac{\mathrm{d}t}{(t+p)\,\sqrt{(t+x)(t+y)(t+z)}}
    
    Args:
        x, y, z (ArrayLike): Real-valued parameter.
        p (ArrayLike): Real-valued parameter. p ∈ ℝ, p ≠ 0.

    Returns:
        Scalar or `numpy.ndarray` broadcast from inputs. Returns the Cauchy principal value if p < 0.

    Raises:
        ValueError: If any of x, y, or z is negative, or more than one of them are zero, or p = 0, or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/elliprj.html" width="100%" height="500px"></iframe>
    
    Special Cases:
        - RJ(x, x, x, x) = 1/(x sqrt(x))
        - RJ(x, y, z, z) = RD(x, y, z)
        - RJ(x, x, x, p) = 3/(x-p) * (RC(x, p) - 1/sqrt(x)) for x ≠ p and xp ≠ 0
        - RJ(x, y, y, y) = RD(x, y, y)
        - RJ(x, y, y, p) = 3/(p-y) * (RC(x, y) - RC(x, p)) for y ≠ p
        - RJ(x, y, z, p) = 0 for x = ∞ or y = ∞ or z = ∞ or p = ∞

    Related Functions:
        - With c = csc²φ and kc² = 1 - m: Π(φ, n, m) = n / 3 * RJ(c - 1, c - m, c, c - n) + F(φ, m)

    Notes:
        The parameters x, y, and z are symmetric. This means swapping them does not change the 
        value of the function. At most one of them can be zero.
    
    References:
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.elliprj, x, y, z, p)


def elliprc(x: ArrayLike, y: ArrayLike) -> FloatArray | float:
    r"""Computes Carlson degenerate integral RC.

    .. math::

        R_C(x, y) = \tfrac{1}{2} \int_0^{\infty} \frac{\mathrm{d}t}{(t+y)\,\sqrt{t+x}}
    
    Args:
        x, y (ArrayLike): Real-valued parameter.

    Returns:
        Scalar or `numpy.ndarray` broadcast from inputs. Returns the Cauchy principal value if y < 0.

    Raises:
        ValueError: If x < 0 or y = 0, or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/elliprc.html" width="100%" height="500px"></iframe>
    
    Special Cases:
        - RC(x, x) = 1/sqrt(x)
        - RC(0, y) = π/(2*sqrt(y))
        - RC(x, y) = atan(sqrt(y-x)/x) / sqrt(y-x) for y > x
        - RC(x, y) = ln(sqrt(x) + sqrt(x-y)) / sqrt(x-y) for y < x
        - RC(x, y) = 0 for x = ∞ or y = ∞

    Related Functions:
        - RC(x, y) = RF(x, y, y)

    Notes:
        RC is a degenerate case of the RF. It is an elementary function rather than an elliptic integral.
    
    References:
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - The SciPy Community. “SciPy: Special Functions - Elliprc.” Accessed April 17, 2025. https://docs.scipy.org/doc/scipy/reference/generated/scipy.special.elliprc.html.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.elliprc, x, y)


def elliprd(x: ArrayLike, y: ArrayLike, z: ArrayLike) -> FloatArray | float:
    r"""Computes Carlson degenerate integral RD.

    .. math::

        R_D(x, y, z) = \tfrac{3}{2} \int_0^{\infty} \frac{\mathrm{d}t}{(t+z)\,\sqrt{(t+x)(t+y)(t+z)}}
    
    Args:
        x, y, z (ArrayLike): Real-valued parameter.

    Returns:
        Scalar or `numpy.ndarray` broadcast from inputs.

    Raises:
        ValueError: If x < 0, y < 0, z ≤ 0 or when both x and y are zero, or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/elliprd.html" width="100%" height="500px"></iframe>
    
    Special Cases:
        - RD(x, x, x) = 1/(x sqrt(x))
        - RD(0, y, y) = 3/4 * π / (y sqrt(y))
        - RD(x, y, y) = 3/(2(y-x)) * (RC(x, y) - sqrt(x)/y) for x ≠ y
        - RD(x, x, z) = 3/(z-x) * (RC(z, x) - 1/sqrt(z)) for x ≠ z
        - RD(x, y, z) = 0 for x = ∞ or y = ∞ or z = ∞

    Related Functions:
        - With c = csc²φ: D(φ, m) = RD(c - 1, c - m, c) / 3

    Notes:
        The parameters x and y (but not z!) are symmetric. This means swapping them does not change the value of the function. At most one of them can be zero.
    
    References:
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.elliprd, x, y, z) 