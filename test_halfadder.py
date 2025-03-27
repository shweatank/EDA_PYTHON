import pytest
def half_adder(a, b):
    """Returns the sum and carry-out for a half-adder."""
    return a ^ b, a & b

# Define all possible cases
ALL_CASES = [(0, 0, 0, 0), (0, 1, 1, 0), (1, 0, 1, 0), (1, 1, 0, 1)]

# Define only tested cases
TESTED_CASES = [(0, 0, 0, 0), (0, 1, 1, 0), (1, 0, 1, 0), (1, 1, 0, 1)]


@pytest.mark.parametrize("a, b, expected_sum, expected_carry", TESTED_CASES)
def test_half_adder(a, b, expected_sum, expected_carry):
    summation, carry_out = half_adder(a, b)
    assert summation == expected_sum, f"Expected sum: {expected_sum}, but got {summation}"
    assert carry_out == expected_carry, f"Expected carry: {expected_carry}, but got {carry_out}"


def test_missing_cases():
    """Check if all cases are covered"""
    tested_inputs = {(a, b) for a, b, _, _ in TESTED_CASES}
    all_inputs = {(a, b) for a, b, _, _ in ALL_CASES}

    missing_cases = all_inputs - tested_inputs
    assert not missing_cases, f"Missing test cases: {missing_cases}"
