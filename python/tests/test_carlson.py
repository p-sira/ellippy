# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

from itertools import permutations

import numpy as np
import pytest
from ellippy import elliprc, elliprd, elliprf, elliprg, elliprj

from tests.common_utils import EPSILON, ellip_test_suite

TestEllipRF = ellip_test_suite(
    elliprf,
    3,
    [
        ("elliprf_data.csv", 1e-15),
    ],
)

TestEllipRG = ellip_test_suite(
    elliprg,
    3,
    [
        ("elliprg_data.csv", 1e-15),
    ],
)

TestEllipRJ = ellip_test_suite(
    elliprj,
    4,
    [
        # Match the pinned ellip crate's bounds for these same Wolfram fixtures.
        ("elliprj_data.csv", 3.1e-15),
        ("elliprj_pv.csv", 5e-14, EPSILON),
    ],
)

TestEllipRC = ellip_test_suite(
    elliprc,
    2,
    [
        ("elliprc_data.csv", 1e-15),
        ("elliprc_pv.csv", 1e-15),
    ],
)

TestEllipRD = ellip_test_suite(
    elliprd,
    3,
    [
        ("elliprd_data.csv", 2e-15),
    ],
)


@pytest.mark.parametrize("scale", [2.0**-600, 1.0, 2.0**600])
def test_elliprg_zero_argument_rounding(scale):
    # Correctly rounded reference for the exact f64 inputs, from 100-digit RG.
    expected = 0.6666666666666674 * np.sqrt(scale)
    inputs = np.array(list(permutations((0.0, EPSILON, 16.0 / 9.0)))) * scale
    for args in inputs:
        np.testing.assert_allclose(elliprg(*args), expected, rtol=3 * EPSILON, atol=0)
    # Exercise both sides of the automatic Rayon cutover through the public API.
    for size in (6, 8192):
        args = np.resize(inputs, (size, 3)).T
        np.testing.assert_allclose(elliprg(*args), expected, rtol=3 * EPSILON, atol=0)
