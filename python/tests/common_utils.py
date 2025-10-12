# EllipPy is licensed under The 3-Clause BSD, see LICENSE.
# Copyright 2025 Sira Pornsiriprasert <code@psira.me>

import pytest
import numpy as np
from pathlib import Path

EPSILON = 2.2204460492503131e-16
TEST_DATA_DIR = Path(__file__).parent / "data" / "wolfram"


def load_test_data(filename):
    """Load test data from CSV file and return as numpy arrays."""
    filepath = TEST_DATA_DIR / filename
    if not filepath.exists():
        pytest.skip(f"Test data file {filename} not found")

    return np.loadtxt(filepath, delimiter=",", dtype=np.float64)


def ellip_test_suite(func, n_args, test_cases):
    """Generate a test class for a function with multiple test cases.

    Usage:
    TestEllipK = ellip_test_suite(ellipk, 1, [
        ("ellipk_data.csv", 5e-15),
        ("ellipk_neg.csv", 5e-14),
    ])
    """

    class TestSuite:
        @pytest.mark.parametrize("filename,rtol", test_cases)
        def test_function(self, filename, rtol):
            data = load_test_data(filename)
            inps = np.array_split(data[:, :n_args], n_args, axis=1)
            expected = data[:, -1]
            result = func(*inps)
            np.testing.assert_allclose(result, expected, rtol=rtol)

    # Set the class name dynamically
    TestSuite.__name__ = f"Test{func.__name__.title()}"
    TestSuite.__qualname__ = f"Test{func.__name__.title()}"

    return TestSuite
