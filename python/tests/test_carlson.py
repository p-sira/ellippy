# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

from ellippy import *
from tests.common_utils import ellip_test_suite

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
        ("elliprj_data.csv", 2e-15),
        ("elliprj_pv.csv", 2e-10),
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
