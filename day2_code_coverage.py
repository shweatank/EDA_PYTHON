from truth_table import*
import pytest

@pytest.mark.parametrize("a,b,expected",[
    (False, False, False),
    (False, True, False),
    (True, False, False),
    (True, True, True)
])
def test_and(a,b,expected):
   assert  and_gate(a,b) == expected


@pytest.mark.parametrize("a,b,expected",[
    (False, False, False),
    (False, True, True),
    (True, False, True),
    (True, True, True)
])
def test_or(a,b,expected):
    assert or_gate(a,b) == expected


def test_not():
    assert not_gate(0) == 1
    assert  not_gate(1) == 0


