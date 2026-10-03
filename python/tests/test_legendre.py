# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

import numpy as np
import pytest
from ellippy.legendre import (
    ellipd,
    ellipdinc,
    ellipe,
    ellipeinc,
    ellipf,
    ellipk,
    ellipke,
    ellippi,
    ellippiinc,
    ellippiinc_bulirsch,
)

from tests.common_utils import ellip_test_suite, load_test_data

TestEllipK = ellip_test_suite(
    ellipk,
    1,
    [
        ("ellipk_data.csv", 5e-15),
        ("ellipk_neg.csv", 5e-14),
    ],
)

TestEllipE = ellip_test_suite(
    ellipe,
    1,
    [
        ("ellipe_data.csv", 1e-15),
        ("ellipe_neg.csv", 5e-16),
    ],
)


class TestEllipKe:
    @pytest.mark.parametrize(
        "k_file,e_file,rtol",
        [
            ("ellipk_data.csv", "ellipe_data.csv", 5e-15),
            ("ellipk_neg.csv", "ellipe_neg.csv", 5e-15),
        ],
    )
    def test_function(self, k_file, e_file, rtol):
        expected_k = load_test_data(k_file)
        expected_e = load_test_data(e_file)
        k, _ = ellipke(expected_k[:, 0])
        _, e = ellipke(expected_e[:, 0])
        np.testing.assert_allclose(k, expected_k[:, -1], rtol=rtol)
        np.testing.assert_allclose(e, expected_e[:, -1], rtol=rtol)


TestEllipPi = ellip_test_suite(
    ellippi,
    2,
    [
        ("ellippi_data.csv", 1e-14),
        ("ellippi_neg.csv", 7e-15),
        ("ellippi_pv.csv", 1e-14),
    ],
)

TestEllipD = ellip_test_suite(
    ellipd,
    1,
    [
        ("ellipd_data.csv", 1e-15),
        ("ellipd_neg.csv", 1e-15),
    ],
)

TestEllipF = ellip_test_suite(
    ellipf,
    2,
    [
        ("ellipf_data.csv", 2e-15),
        ("ellipf_neg.csv", 1e-15),
    ],
)

TestEllipEinc = ellip_test_suite(
    ellipeinc,
    2,
    [
        ("ellipeinc_data.csv", 1e-14),
        ("ellipeinc_neg.csv", 1e-15),
    ],
)

TestEllipPiInc = ellip_test_suite(
    ellippiinc,
    3,
    [
        ("ellippiinc_data.csv", 5e-14),
        ("ellippiinc_neg.csv", 1e-14),
        ("ellippiinc_pv.csv", 5e-13),
    ],
)


TestEllipDInc = ellip_test_suite(
    ellipdinc,
    2,
    [
        ("ellipdinc_data.csv", 2e-15),
        ("ellipdinc_neg.csv", 1e-15),
    ],
)

TestEllipPiIncBulirsch = ellip_test_suite(
    ellippiinc_bulirsch,
    3,
    [
        ("ellippiinc_data.csv", 5e-14),
        ("ellippiinc_neg.csv", 1e-14),
        ("ellippiinc_pv.csv", 5e-13),
    ],
)
