import pytest
from half_adder import half_adder

test_cases = [(a, b, (a ^ b, a & b)) for a in [0, 1] for b in [0, 1]]
@pytest.mark.parametrize("a, b, expected", test_cases)
def test_half_adder(a, b, expected):
    output = half_adder(a, b)
    assert output == expected