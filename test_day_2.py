import pytest
from day_1 import logic_and, logic_or, logic_not
@pytest.mark.parametrize("a,b,expected", [(0, 0, 0),(0, 1, 0),(1, 0, 0),(1, 1, 1)])
def test_logic_and(a, b, expected):
    assert logic_and(a, b) == expected
@pytest.mark.parametrize("a,b,expected", [(0, 0, 0),(0, 1, 1),(1, 0, 1),(1, 1, 1)])
def test_logic_or(a, b, expected):
    assert logic_or(a, b) == expected
@pytest.mark.parametrize("a,expected", [(0, 1),(1, 0),])
def test_logic_not(a, expected):
    assert logic_not(a) == expected
