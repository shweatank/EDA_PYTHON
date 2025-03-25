
from eda import and_gate,or_gate,not_gate,nand_gate,nor_gate
import pytest
@pytest.mark.parametrize("a,b,result",[(0,0,0),(0,1,0),(1,0,0),(1,1,1)])
def test_and(a,b,result):
    assert and_gate(a,b)==result

@pytest.mark.parametrize("a,b,result", [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)])
def test_or(a,b,result):
    assert or_gate(a,b)==result

def test_not():
    assert not_gate(0)==1
    assert not_gate(1)==0

@pytest.mark.parametrize("a,b,result",[(0,0,1),(0,1,1),(1,0,1),(1,1,0)])
def test_nand(a,b,result):
    assert nand_gate(a,b)==result

@pytest.mark.parametrize("a,b,result", [(0, 0, 1), (0, 1, 0), (1, 0, 0),(1, 1, 0)])
def test_nor(a,b,result):
    assert nor_gate(a,b)==result

