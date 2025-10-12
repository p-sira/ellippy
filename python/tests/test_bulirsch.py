# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

from ellippy import *
from tests.common_utils import ellip_test_suite

TestCel = ellip_test_suite(
    cel,
    4,
    [
        ("cel_data.csv", 1e-14),
        ("cel_pv.csv", 1e-14),
    ],
)

TestCel1 = ellip_test_suite(
    cel1,
    1,
    [
        ("cel1_data.csv", 2e-15),
    ],
)

TestCel2 = ellip_test_suite(
    cel2,
    3,
    [
        ("cel2_data.csv", 1e-15),
    ],
)

TestEl1 = ellip_test_suite(
    el1,
    2,
    [
        ("el1_data.csv", 1e-15),
    ],
)

TestEl2 = ellip_test_suite(
    el2,
    4,
    [
        ("el2_data.csv", 2e-14),
    ],
)

TestEl3 = ellip_test_suite(
    el3,
    3,
    [
        ("el3_data.csv", 2e-14),
        ("el3_pv.csv", 5e-15),
    ],
)
