# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

"""
Elliptic integral functions in Bulirsch's form.
"""

from numpy.typing import ArrayLike
from . import _ellip
from ._ellip import FloatArray, returnfloat, returnfloat_single


def cel(kc: ArrayLike, p: ArrayLike, a: ArrayLike, b: ArrayLike) -> FloatArray | float:
    r"""Computes general complete elliptic integral in Bulirsch form ``cel``.

    .. math::

        \mathrm{cel}(k_c, p, a, b) = \int_0^{\pi/2} \frac{a\cos^2\theta + b\sin^2\theta}{(\cos^2\theta + p\sin^2\theta)\,\sqrt{\cos^2\theta + k_c^2\sin^2\theta}}\,\mathrm{d}\theta

    Args:
        kc (ArrayLike): Complementary modulus. kc ∈ ℝ, kc ≠ 0.
        p (ArrayLike): Characteristic parameter. p ∈ ℝ, p ≠ 0.
        a, b (ArrayLike): Real-valued coefficient.

    Returns:
        Scalar or `numpy.ndarray` with the same shape as `kc`.

    Raises:
        ValueError: If kc = 0, p = 0, more than one argument is infinite, or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/cel.html" width="100%" height="500px"></iframe>

    Special Cases:
        - cel(kc, p, 0, 0) = 0
        - cel(kc, p, a, b) = 0 for \|kc\| = ∞
        - cel(kc, p, a, b) = 0 for \|p\| = ∞
        - cel(kc, p, a, b) = sign(a) ∞ for \|a\| = ∞
        - cel(kc, p, a, b) = sign(b) ∞ for \|b\| = ∞

    Related Functions:
        With kc² = 1 - m and p = 1 - n:
            - K(m) = cel(kc, 1, 1, 1) = cel1(kc)
            - E(m) = cel(kc, 1, 1, kc²) = cel2(kc, 1, kc²)
            - D(m) = cel(kc, 1, 0, 1)
            - Π(n, m) = cel(kc, p, 1, 1)

    References:
        - Bulirsch, R. “Numerical Calculation of Elliptic Integrals and Elliptic Functions. III.” Numerische Mathematik 13, no. 4 (August 1, 1969): 305-15. https://doi.org/10.1007/BF02165405.
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.cel, kc, p, a, b)


def cel1(kc: ArrayLike) -> FloatArray | float:
    r"""Computes Bulirsch complete integral of the first kind ``cel1``.

    .. math::

        \mathrm{cel1}(k_c) = \int_0^{\pi/2} \frac{\mathrm{d}\theta}{\sqrt{\cos^2\theta + k_c^2\sin^2\theta}}

    Args:
        kc (ArrayLike): Complementary modulus. kc ∈ ℝ, kc ≠ 0.

    Returns:
        Scalar or `numpy.ndarray` with the same shape as `kc`.

    Raises:
        ValueError: If kc = 0 or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/cel1.html" width="100%" height="500px"></iframe>

    Special Cases:
        - cel1(kc) = 0 for \|kc\| = ∞

    Related Functions:
        - With kc² = 1 - m: K(m) = cel(kc, 1, 1, 1) = cel1(kc)

    References:
        - Bulirsch, Roland. “Numerical Calculation of Elliptic Integrals and Elliptic Functions.” Numerische Mathematik 7, no. 1 (February 1, 1965): 78-90. https://doi.org/10.1007/BF01397975.
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat_single(_ellip.cel1, kc)


def cel2(kc: ArrayLike, a: ArrayLike, b: ArrayLike) -> FloatArray | float:
    r"""Computes Bulirsch complete integral of the second kind ``cel2``.

    .. math::

        \mathrm{cel2}(k_c, a, b) = \int_{0}^{\pi/2}\frac{a + b\,\tan^2\theta}{\sqrt{(1+\tan^2\theta)(1+k_c^2\tan^2\theta)}} \,\mathrm{d}\theta

    Args:
        kc (ArrayLike): Complementary modulus. kc ∈ ℝ, kc ≠ 0.
        a, b (ArrayLike): Real-valued coefficient.

    Returns:
        Scalar or `numpy.ndarray` with the same shape as `kc`.

    Raises:
        ValueError: If kc = 0, more than one arguments are infinite, or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/cel2.html" width="100%" height="500px"></iframe>

    Special Cases:
        - cel2(kc, 0, 0) = 0
        - cel(kc, a, b) = 0 for \|kc\| = ∞
        - cel(kc, a, b) = sign(a) ∞ for \|a\| = ∞
        - cel(kc, a, b) = sign(b) ∞ for \|b\| = ∞

    Related Functions:
        - cel2(kc, a, b) = cel(kc, 1, a, b)
        - With kc² = 1 - m: E(m) = cel(kc, 1, 1, kc²) = cel2(kc, 1, kc²)

    References:
        - Bulirsch, Roland. “Numerical Calculation of Elliptic Integrals and Elliptic Functions.” Numerische Mathematik 7, no. 1 (February 1, 1965): 78-90. https://doi.org/10.1007/BF01397975.
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.cel2, kc, a, b)


def el1(x: ArrayLike, kc: ArrayLike) -> FloatArray | float:
    r"""Computes Bulirsch incomplete integral of the first kind ``el1``.

    .. math::

        \mathrm{el1}(x, k_c) = \int_0^{\arctan x} \frac{\mathrm{d}\theta}{\sqrt{\cos^2\theta + k_c^2\sin^2\theta}}

    Args:
        x (ArrayLike): Tangent of amplitude angle, x ∈ ℝ, x = tan(φ).
        kc (ArrayLike): Complementary modulus. kc ∈ ℝ, kc ≠ 0.

    Returns:
        Scalar or `numpy.ndarray` broadcast from inputs.

    Raises:
        ValueError: If kc = 0 or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/el1.html" width="100%" height="500px"></iframe>

    Special Cases:
        - el1(0, kc) = 0
        - el1(∞, kc) = cel1(kc)
        - el1(x, ∞) = 0

    Related Functions:
        With x = tan φ and kc² = 1 - m:
            - F(φ, m) = el1(x, kc) = el2(x, kc, 1, 1)
            - el1(∞, kc) = cel1(kc)

    References:
        - Bulirsch, Roland. “Numerical Calculation of Elliptic Integrals and Elliptic Functions.” Numerische Mathematik 7, no. 1 (February 1, 1965): 78-90. https://doi.org/10.1007/BF01397975.
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.el1, x, kc)


def el2(x: ArrayLike, kc: ArrayLike, a: ArrayLike, b: ArrayLike) -> FloatArray | float:
    r"""Computes Bulirsch incomplete integral of the second kind ``el2``.

    .. math::

        \mathrm{el2}(x, k_c, a, b) = \int_{0}^{\arctan x}\frac{a + b\,\tan^2\theta}{\sqrt{(1+\tan^2\theta)(1+k_c^2\tan^2\theta)}} \,\mathrm{d}\theta

    Args:
        x (ArrayLike): Tangent of amplitude angle, x ∈ ℝ, x = tan(φ).
        kc (ArrayLike): Complementary modulus. kc ∈ ℝ, kc ≠ 0.
        a, b (ArrayLike): Real-valued coefficient.

    Returns:
        Scalar or `numpy.ndarray` broadcast from inputs.

    Raises:
        ValueError: If kc = 0 or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/el2.html" width="100%" height="500px"></iframe>

    Special Cases:
        - el2(0, kc, a, b) = 0
        - el2(x, kc, 0, 0) = 0
        - el2(∞, kc, a, b) = cel2(kc, a, b)

    Related Functions:
        With x = tan φ and kc² = 1 - m,
            - F(φ, m) = el1(x, kc) = el2(x, kc, 1, 1)
            - E(φ, m) = el2(x, kc, 1, kc²)
            - el2(∞, kc, a, b) = cel2(kc, a, b)

    References:
        - Bulirsch, Roland. “Numerical Calculation of Elliptic Integrals and Elliptic Functions.” Numerische Mathematik 7, no. 1 (February 1, 1965): 78-90. https://doi.org/10.1007/BF01397975.
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.el2, x, kc, a, b)


def el3(x: ArrayLike, kc: ArrayLike, p: ArrayLike) -> FloatArray | float:
    r"""Computes Bulirsch incomplete integral of the third kind ``el3``.

    .. math::

        \mathrm{el3}(x, k_c, p) = \int_0^{\arctan x} \frac{\mathrm{d}\theta}{\left(\cos^2\theta + p\sin^2\theta\right)\,\sqrt{\cos^2\theta + k_c^2\sin^2\theta}}

    Args:
        x (ArrayLike): Tangent of amplitude angle, x ∈ ℝ, x = tan(φ).
        kc (ArrayLike): Complementary modulus. kc ∈ ℝ, kc ≠ 0.
        p (ArrayLike): Characteristic parameter. p ∈ ℝ, p ≠ 0.

    Returns:
        Scalar or `numpy.ndarray` broadcast from inputs. Returns the Cauchy principal value when 1 + px² < 0.

    Raises:
        ValueError: If kc = 0, 1 + px² = 0, \|kc\| > 1 for p < 0, or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/el3.html" width="100%" height="500px"></iframe>

    Special Cases:
        - el3(0, kc, p) = 0
        - el3(∞, kc, p) = cel(kc, p, 1, 1) = Π(1-p, 1-kc²)

    Related Functions:
        With x = tan φ, p = 1 - n and kc² = 1 - m:
            - Π(φ, n, m) = el3(x, kc, p)
            - el3(∞, kc, p) = cel(kc, p, 1, 1) = Π(n, m)

    References:
        - Bulirsch, R. “Numerical Calculation of Elliptic Integrals and Elliptic Functions. III.” Numerische Mathematik 13, no. 4 (August 1, 1969): 305-15. https://doi.org/10.1007/BF02165405.
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.el3, x, kc, p)
