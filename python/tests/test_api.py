# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

import ellippy as ep
import numpy as np
import pytest


def test_ellippiinc_signature_and_keywords():
    val_pos = ep.ellippiinc(np.pi / 4, 0.1, 0.25)
    val_kw = ep.ellippiinc(phi=np.pi / 4, n=0.1, m=0.25)
    assert isinstance(val_pos, float)
    assert isinstance(val_kw, float)
    assert np.isclose(val_pos, 0.8197192266707629)
    assert np.isclose(val_kw, 0.8197192266707629)


def test_ellippiinc_bulirsch_signature_and_keywords():
    val_pos = ep.ellippiinc_bulirsch(np.pi / 4, 0.1, 0.25)
    val_kw = ep.ellippiinc_bulirsch(phi=np.pi / 4, n=0.1, m=0.25)
    assert isinstance(val_pos, float)
    assert isinstance(val_kw, float)
    assert np.isclose(val_pos, 0.8197192266707629)
    assert np.isclose(val_kw, 0.8197192266707629)


def test_scalar_return_types():
    assert isinstance(ep.ellipk(0), float)
    assert isinstance(ep.ellipk(np.int64(0)), float)
    assert isinstance(ep.ellipk(np.float64(0.5)), float)
    assert isinstance(ep.cel1(1), float)
    assert isinstance(ep.cel3(1, 1), float)
    assert isinstance(ep.elliprf(1, 1, 1), float)
    assert isinstance(ep.jacobi_zeta(0, 0.5), float)

    k, e = ep.ellipke(0.5)
    assert isinstance(k, float)
    assert isinstance(e, float)


def test_ellipke_and_cel3():
    # ellipke returns (K, E), which must agree with ellipk and ellipe.
    k, e = ep.ellipke(np.array([0.1, 0.2, 0.3]))
    assert isinstance(k, np.ndarray)
    assert isinstance(e, np.ndarray)
    np.testing.assert_allclose(k, ep.ellipk([0.1, 0.2, 0.3]))
    np.testing.assert_allclose(e, ep.ellipe([0.1, 0.2, 0.3]))

    # cel3(kc, p) = cel(kc, p, 1, 1), and cel3(kc, 1) = cel1(kc).
    np.testing.assert_allclose(
        ep.cel3([0.5, 0.5], [0.25, 1.0]),
        ep.cel([0.5, 0.5], [0.25, 1.0], [1.0, 1.0], [1.0, 1.0]),
    )
    np.testing.assert_allclose(ep.cel3(0.5, 1.0), ep.cel1(0.5))


def test_value_errors():
    with pytest.raises(ValueError):
        ep.ellipk(2.0)

    with pytest.raises(ValueError):
        ep.cel(0.0, 1.0, 1.0, 1.0)

    with pytest.raises(ValueError):
        ep.cel3(0.0, 1.0)

    with pytest.raises(ValueError):
        ep.ellipke(2.0)

    with pytest.raises(ValueError):
        ep.elliprf(-1.0, 1.0, 1.0)
