from gates import or_gate,and_gate,not_gate
import pytest

def and_gate(x, y):
    return [x[i] & y[i] for i in range(len(x))]

def or_gate(x, y):
    return [x[i] | y[i] for i in range(len(x))]

def not_gate(x):
    return [1 - x[i] for i in range(len(x))]

@pytest.mark.parametrize("x, y, expected", [
    ([0, 0, 1, 1], [0, 1, 0, 1], [0, 0, 0, 1]),
    ([1, 1, 1, 0], [1, 0, 0, 0], [1, 0, 0, 0])
])
def test_and_gate(x, y, expected):
    assert and_gate(x, y) == expected

@pytest.mark.parametrize("x, y, expected", [
    ([0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 1]),
    ([1, 1, 1, 0], [1, 0, 0, 0], [1, 1, 1, 0])
])
def test_or_gate(x, y, expected):
    assert or_gate(x, y) == expected

@pytest.mark.parametrize("x, expected", [
    ([0, 1, 0, 1], [1, 0, 1, 0]),
    ([1, 1, 0, 0], [0, 0, 1, 1])
])
def test_not_gate(x, expected):
    assert not_gate(x) == expected





