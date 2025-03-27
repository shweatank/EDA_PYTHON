import time
import pytest
from logicgates import AND, OR, NOT, XOR, NAND, NOR, XNOR

LOG_FILE = "Execution_time.log"

def log_result(message):
    """Function to log test results to a file."""
    with open(LOG_FILE, "a") as log:
        log.write(message + "\n")

def measure_time(func, *args):
    """Measure execution time of a function."""
    start_time = time.perf_counter()
    result = func(*args)
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    return result, execution_time

@pytest.mark.parametrize("a,b,c", [(0,0,0), (0,1,0), (1,0,0), (1,1,1)])
def test_and(a, b, c):
    result, exec_time = measure_time(AND, a, b)
    message = f"AND({a}, {b}) -> Output: {result}, Execution Time: {exec_time:.10f} sec"
    print(message)
    log_result(message)
    assert result == c

@pytest.mark.parametrize("a,b,c", [(0,0,0), (0,1,1), (1,0,1), (1,1,1)])
def test_or(a, b, c):
    result, exec_time = measure_time(OR, a, b)
    message = f"OR({a}, {b}) -> Output: {result}, Execution Time: {exec_time:.10f} sec"
    print(message)
    log_result(message)
    assert result == c

def test_not():
    for a, expected in [(0, 1), (1, 0)]:
        result, exec_time = measure_time(NOT, a)
        message = f"NOT({a}) -> Output: {int(result)}, Execution Time: {exec_time:.10f} sec"
        print(message)
        log_result(message)
        assert result == expected

@pytest.mark.parametrize("a,b,c", [(0,0,1), (0,1,1), (1,0,1), (1,1,0)])
def test_nand(a, b, c):
    result, exec_time = measure_time(NAND, a, b)
    message = f"NAND({a}, {b}) -> Output: {int(result)}, Execution Time: {exec_time:.10f} sec"
    print(message)
    log_result(message)
    assert result == c

@pytest.mark.parametrize("a,b,c", [(0,0,1), (0,1,0), (1,0,0), (1,1,0)])
def test_nor(a, b, c):
    result, exec_time = measure_time(NOR, a, b)
    message = f"NOR({a}, {b}) -> Output: {int(result)}, Execution Time: {exec_time:.10f} sec"
    print(message)
    log_result(message)
    assert result == c

@pytest.mark.parametrize("a,b,c", [(0,0,0), (0,1,1), (1,0,1), (1,1,0)])
def test_xor(a, b, c):
    result, exec_time = measure_time(XOR, a, b)
    message = f"XOR({a}, {b}) -> Output: {result}, Execution Time: {exec_time:.10f} sec"
    print(message)
    log_result(message)
    assert result == c

@pytest.mark.parametrize("a,b,c", [(0,0,1), (0,1,0), (1,0,0), (1,1,1)])
def test_xnor(a, b, c):
    result, exec_time = measure_time(XNOR, a, b)
    message = f"XNOR({a}, {b}) -> Output: {int(result)}, Execution Time: {exec_time:.10f} sec"
    print(message)
    log_result(message)
    assert result == c
