import pytest
from gates import not_gate,or_gate,and_gate

test_cases = [(a, b, a & b) for a in [0, 1] for b in [0, 1]]
@pytest.mark.parametrize("a, b, expected", test_cases)
def test_and(a,b,expected):
    output=and_gate(a,b)
    assert output==expected

test_cases = [(a, b, a | b) for a in [0, 1] for b in [0, 1]]
@pytest.mark.parametrize("a, b, expected", test_cases)
def test_or(a,b,expected):
    output=or_gate(a,b)
    assert output==expected


@pytest.mark.parametrize("a,expected", [
    (0,1),       # Test case 1
    (1,0),       # Test case 2
])
def test_not(a,expected):
    output=not_gate(a)
    assert output==expected




