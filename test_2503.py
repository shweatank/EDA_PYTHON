import pytest
from day_2503 import func_or,func_and,comp

def test_func_or():
    print(func_or([[0,0],[0,1],[1,0],[1,1]]))
    assert func_or([[0,0],[0,1],[1,0],[1,1]])==[0,1,1,1]
    # assert func_or()
def test_func_and():
    print(func_and([[0,0],[0,1],[1,0],[1,1]]))
    assert func_and([[0,0],[0,1],[1,0],[1,1]])==[0,0,0,1]

def test_func_comp():
    assert comp(0)==1
    assert  comp(1)==0

test_func_or()
test_func_and()