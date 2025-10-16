# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

"""
Elliptic integral functions in Legendre's form.
"""

from numpy.typing import ArrayLike
from . import _ellip
from ._ellip import FloatArray, returnfloat, returnfloat_single


def ellipk(m: ArrayLike) -> FloatArray | float:
    r"""Computes complete elliptic integral of the first kind K(m).

    .. math::

        K(m) = \int_0^{\pi/2} \frac{\mathrm{d}\theta}{\sqrt{1 - m\,\sin^2\theta}}

    Args:
        m (ArrayLike): Elliptic parameter. m ∈ ℝ, m ≤ 1.

    Returns:
        Scalar or `numpy.ndarray` with the same shape as `m`.

    Raises:
        ValueError: If m > 1 or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/ellipk.html" width="100%" height="500px"></iframe>

    Special Cases:
        - K(0) = π/2
        - K(1) = ∞
        - K(-∞) = 0

    Related Functions:
        - K(m) = RF(0, 1 - m, 1).
        - F(π/2, m) = K(m).

    Notes:
        The elliptic modulus k is frequently used instead of the parameter m,
        where k² = m.

    References:
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat_single(_ellip.ellipk, m)


def ellipe(m: ArrayLike) -> FloatArray | float:
    r"""Computes complete elliptic integral of the second kind E(m).

    .. math::

        E(m) = \int_0^{\pi/2} \sqrt{1 - m\,\sin^2\theta}\,\mathrm{d}\theta

    Args:
        m (ArrayLike): Elliptic parameter. m ∈ ℝ, m ≤ 1.

    Returns:
        Scalar or `numpy.ndarray` with the same shape as `m`.

    Raises:
        ValueError: If m > 1 or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/ellipe.html" width="100%" height="500px"></iframe>

    Special Cases:
        - E(0) = π/2
        - E(1) = 1
        - E(-∞) = ∞

    Related Functions:
        - E(m) = 2·RG(0, 1 - m, 1).
        - E(π/2, m) = E(m).

    Notes:
        The elliptic modulus k is frequently used instead of the parameter m,
        where k² = m.

    References:
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Abramowitz, Milton, and Irene A. Stegun. Handbook of Mathematical Functions: With Formulas, Graphs and Mathematical Tables. Unabridged, Unaltered and corr. Republ. of the 1964 ed. With Conference on mathematical tables, National science foundation, and Massachusetts institute of technology. Dover Books on Advanced Mathematics. Dover publ, 1972.
        - The SciPy community. “Scipy.Special.Ellipe — SciPy v1.16.0 Manual.” Accessed July 28, 2025. https://docs.scipy.org/doc/scipy-1.16.0/reference/generated/scipy.special.ellipe.html.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat_single(_ellip.ellipe, m)


def ellippi(n: ArrayLike, m: ArrayLike) -> FloatArray | float:
    r"""Computes complete elliptic integral of the third kind Π(n | m).

    .. math::

        \Pi(n\,|\,m) = \int_0^{\pi/2} \frac{\mathrm{d}\theta}{\left(1 - n\,\sin^2\theta\right)\,\sqrt{1 - m\,\sin^2\theta}}

    Args:
        n (ArrayLike): Characteristic. n ∈ ℝ, n ≠ 1.
        m (ArrayLike): Elliptic parameter. m ∈ ℝ, m ≤ 1.

    Returns:
        Scalar or `numpy.ndarray` broadcast from `n` and `m`. Returns the Cauchy principal value if n > 1.

    Raises:
        ValueError: If n = 1, m > 1, or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/ellippi_3d.html" width="100%" height="650px"></iframe>

    Special Cases:
        - Π(0, 0) = π/2
        - Π(0, m) = K(m)
        - Π(n, 0) = π/(2\sqrt{1-n}) for n < 1
        - Π(n, 0) = 0 for n > 1
        - Π(n, m) = ∞ as n → 1-
        - Π(n, 1) = sign(1-n) · ∞
        - Π(±∞, m) = 0
        - Π(n, -∞) = 0

    Related Functions:
        - Π(n, m) = (n/3)·RJ(0, 1 - m, 1, 1 - n) + K(m)
        - Π(n, n) = E(n)/(1 - n) for n < 1
        - Π(n, m) = K(m) - E(m)/(1 - m) for n → 1+

    Notes:
        - The elliptic modulus k is frequently used instead of the parameter m, where k² = m.
        - The characteristic n is sometimes expressed in term of α, where α² = n.

    References:
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.ellippi, n, m)


def ellipd(m: ArrayLike) -> FloatArray | float:
    r"""Computes complete elliptic integral of Legendre's type D(m).

    .. math::

        D(m) = \int_0^{\pi/2} \frac{\sin^2\theta}{\sqrt{1 - m\,\sin^2\theta}}\,\mathrm{d}\theta

    Args:
        m (ArrayLike): Elliptic parameter. m ∈ ℝ, m ≤ 1.

    Returns:
        Scalar or `numpy.ndarray` with the same shape as `m`.

    Raises:
        ValueError: If m > 1 or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/ellipd.html" width="100%" height="500px"></iframe>

    Special Cases:
        - D(0) = π/4
        - D(1) = ∞
        - D(-∞) = 0

    Related Functions:
        - D(m) = (K(m) - E(m)) / m
        - D(m) = RD(0, 1 - m, 1) / 3
        - D(π/2, m) = D(m)

    Notes:
        The elliptic modulus k is frequently used instead of m, where k² = m.

    References:
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat_single(_ellip.ellipd, m)


def ellipf(phi: ArrayLike, m: ArrayLike) -> FloatArray | float:
    r"""Computes incomplete elliptic integral of the first kind F(φ | m).

    .. math::

        F(\varphi\,|\,m) = \int_0^{\varphi} \frac{\mathrm{d}\theta}{\sqrt{1 - m\,\sin^2\theta}}

    Args:
        phi (ArrayLike): Amplitude angle (φ) in radians. φ ∈ ℝ. 
        m (ArrayLike): Elliptic parameter. m ∈ ℝ.

    Returns:
        Scalar or `numpy.ndarray` broadcast from `phi` and `m`.

    Raises:
        ValueError: If m sin²φ > 1 or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/ellipf.html" width="100%" height="500px"></iframe>

    Special Cases:
        - F(0, m) = 0
        - F(φ, 0) = φ
        - F(π/2, m) = K(m)
        - F(φ, -∞) = 0
        - F(φ, m) = sign(φ) ∞ for \|φ\| = ∞

    Related Functions:
        - With c = csc²φ: F(φ, m) = RF(c - 1, c - m, c)

    Notes:
        The elliptic modulus k is frequently used instead of the parameter m, where k² = m.

    References:
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - The MathWorks, Inc. “ellipticF.” Accessed April 21, 2025. https://www.mathworks.com/help/symbolic/sym.ellipticf.html.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.ellipf, phi, m)


def ellipeinc(phi: ArrayLike, m: ArrayLike) -> FloatArray | float:
    r"""Computes incomplete elliptic integral of the second kind E(φ | m).

    .. math::

        E(\varphi\,|\,m) = \int_0^{\varphi} \sqrt{1 - m\,\sin^2\theta}\,\mathrm{d}\theta

    Args:
        phi (ArrayLike): Amplitude angle (φ) in radians. φ ∈ ℝ. 
        m (ArrayLike): Elliptic parameter. m ∈ ℝ.

    Returns:
        Scalar or `numpy.ndarray` broadcast from `phi` and `m`.

    Raises:
        ValueError: If m sin²φ > 1 or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/ellipeinc.html" width="100%" height="500px"></iframe>

    Special Cases:
        - E(0, m) = 0
        - E(φ, 0) = φ
        - E(π/2, m) = E(m)
        - E(φ, 1) = sin(φ)
        - E(φ, -∞) = ∞
        - E(±∞, m) = ±∞

    Related Functions:
        - With c = csc²φ: E(φ, m) = RF(c - 1, c - m, c) - m/3 · RD(c - 1, c - m, c)

    Notes:
        The elliptic modulus k is frequently used instead of the parameter m, where k² = m.

    References:
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - The MathWorks, Inc. “ellipticE.” Accessed April 21, 2025. https://www.mathworks.com/help/symbolic/sym.elliptice.html.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.ellipeinc, phi, m)


def ellippiinc(n: ArrayLike, phi: ArrayLike, m: ArrayLike) -> FloatArray | float:
    r"""Computes incomplete elliptic integral of the third kind Π(n; φ | m).

    .. math::

        \Pi(n;\,\varphi\,|\,m) = \int_0^{\varphi} \frac{\mathrm{d}\theta}{\left(1 - n\,\sin^2\theta\right)\,\sqrt{1 - m\,\sin^2\theta}}

    Args:
        n (ArrayLike): Characteristic. n ∈ ℝ, n ≠ 1.
        phi (ArrayLike): Amplitude angle (φ) in radians. φ ∈ ℝ. 
        m (ArrayLike): Elliptic parameter. m ∈ ℝ.

    Returns:
        Scalar or `numpy.ndarray` broadcast from `n`, `phi`, and `m`. Returns the Cauchy principal value if n sin²φ > 1.

    Raises:
        ValueError: If m sin²φ > 1, n sin²φ = 1, m ≥ 1 with φ not a multiple of π/2, or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/ellippiinc_3d.html" width="100%" height="650px"></iframe>

    Special Cases:
        - Π(0, n, m) = 0
        - Π(φ, 0, 0) = φ
        - Π(φ, 1, 0) = tan(φ)
        - Π(φ, 0, m) = F(φ, m)

    Related Functions:
        - Π(φ, 0, m) = F(φ, m)
        - With c = csc²φ: Π(φ, n, m) = (n/3) · RJ(c - 1, c - m, c, c - n) + F(φ, m)
        - With x = tan φ, p = 1 - n, and k_c² = 1 - m: Π(φ, n, m) = el3(x, k_c, p)

    Notes:
        - The elliptic modulus k is frequently used instead of m, where k² = m.
        - The characteristic n is sometimes expressed in term of α, where α² = n.
        - This function `ellippiinc` (of the package) is the circular or hyperbolic case of Π,
          since n and m are real. It is called circular if n·(n - m)·(n - 1) is negative and
          hyperbolic if it is positive.

    References:
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Wolfram Research. “EllipticPi.” 2022. https://reference.wolfram.com/language/ref/EllipticPi.html.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.ellippiinc, n, phi, m)


def ellipdinc(phi: ArrayLike, m: ArrayLike) -> FloatArray | float:
    r"""Computes incomplete elliptic integral of Legendre's type D(φ | m).

    .. math::

        D(\varphi\,|\,m) = \int_0^{\varphi} \frac{\sin^2\theta}{\sqrt{1 - m\,\sin^2\theta}}\,\mathrm{d}\theta

    Args:
        phi (ArrayLike): Amplitude angle (φ) in radians. φ ∈ ℝ. 
        m (ArrayLike): Elliptic parameter. m ∈ ℝ.

    Returns:
        Scalar or `numpy.ndarray` broadcast from `phi` and `m`.

    Raises:
        ValueError: If m sin²φ > 1 or inputs contain NaN.

    Graph:
        .. raw:: html

            <iframe src="./../_static/figures/ellipdinc.html" width="100%" height="500px"></iframe>

    Special Cases:
        - D(0, m) = 0
        - D(π/2, m) = D(m)
        - D(φ, -∞) = 0
        - D(±∞, m) = ±∞

    Related Functions:
        With c = csc²φ,
            - D(φ, m) = (F(φ, m) - E(φ, m)) / m
            - D(φ, m) = RD(c - 1, c - m, c) / 3

    Notes:
        The elliptic modulus k is frequently used instead of m, where k² = m.

    References:
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Maddock, John, Paul Bristow, Hubert Holin, and Xiaogang Zhang. “Boost Math Library: Special Functions - Elliptic Integrals.” Accessed April 17, 2025. https://www.boost.org/doc/libs/1_88_0/libs/math/doc/html/math_toolkit/ellint.html.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.ellipdinc, phi, m)


def ellippiinc_bulirsch(
    n: ArrayLike, phi: ArrayLike, m: ArrayLike
) -> FloatArray | float:
    r"""Computes incomplete elliptic integral of the third kind using the Bulirsch algorithm.

    This is typically about 2x as fast as the standard implementation for non-PV cases
    and m < 1 cases, while maintaining similar accuracy. Otherwise, it delegates
    to :func:`ellippiinc`.

    Args:
        n (ArrayLike): Characteristic. n ∈ ℝ, n ≠ 1.
        phi (ArrayLike): Amplitude angle (φ) in radians. φ ∈ ℝ. 
        m (ArrayLike): Elliptic parameter. m ∈ ℝ.

    Returns:
        Scalar or `numpy.ndarray` broadcast from `n`, `phi`, and `m`.

    Notes:
        See :func:`ellippiinc` for definitions, domains, and relationships.

    References:
        - Carlson, B. C. “DLMF: Chapter 19 Elliptic Integrals.” Accessed February 19, 2025. https://dlmf.nist.gov/19.
        - Pornsiriprasert, Sira. Ellip: Elliptic Integrals for Rust. V. 0.5.1. Released October 10, 2025. https://docs.rs/ellip/0.5.1/ellip/index.html.
    """
    return returnfloat(_ellip.ellippiinc_bulirsch, n, phi, m)
