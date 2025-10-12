# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

from ellippy import *
from tests.common_utils import ellip_test_suite

TestJacobiZeta = ellip_test_suite(
    jacobi_zeta,
    2,
    [
        ("jacobi_zeta_data.csv", 3e-15),
        ("jacobi_zeta_neg.csv", 3e-15),
    ],
)

TestHeumanLambda = ellip_test_suite(
    heuman_lambda,
    2,
    [
        ("heuman_lambda_data.csv", 3e-15),
    ],
)
