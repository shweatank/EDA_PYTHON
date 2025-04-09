import pytest
from logic_gates import *


@pytest.mark.parametrize("a,b,y",[
    (0,0,0),
    (0,1,0),
    (1,0,0),
    (1,1,1)
        ])
def test_and_gate(a,b,y):
    assert  and_gate(a,b) == y



@pytest.mark.parametrize("a,b,y",[
    (0,0,0),
    (0,1,1),
    (1,0,1),
    (1,1,1)
])

def test_or_gate(a,b,y):
    assert  or_gate(a,b) == y


@pytest.mark.parametrize("a,b,y",[
    (0,0,1),
    (1,0,0),
    (0,1,0),
    (1,1,0)
])

def test_nor_gate(a,b,y):
    assert  nor_gate(a,b) == y

@pytest.mark.parametrize("a,b,y",[
    (0,0,1),
    (1,0,1),
    (0,1,1),
    (1,1,0)
])

def test_nand_gate(a,b,y):
    assert  nand_gate(a,b) == y


@pytest.mark.parametrize("a,b,y",[
    (0,0,0),
    (1,0,1),
    (0,1,1),
    (1,1,0)
])

def test_xor_gate(a,b,y):
    assert xor_gate(a,b) == y


@pytest.mark.parametrize("a,b,y",[
    (0,0,1),
    (0,1,0),
    (1,0,0),
    (1,1,1)
])
def test_xnor_gate(a,b,y):
    assert xnor_gate(a,b)==y









