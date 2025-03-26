import pytest
import time
from Half_adder import half_adder, half_adder_carry

LOG_FILE = "test_half_adder.log"

def log_message(message):
    """Writes log messages to a file using `with open()`."""
    with open(LOG_FILE, "a") as log_file:  # Open in append mode
        log_file.write(message + "\n")


@pytest.mark.parametrize("a,b,result", [(0,0,0), (0,1,1), (1,0,1), (1,1,0)])
def test_half_adder(a, b, result):
    start_time = time.time()
    output = half_adder(a, b)
    end_time = time.time()
    execution_time = end_time - start_time

    log_message(f"TEST: half_adder({a}, {b}) -> Expected: {result}, Got: {output}, Execution Time: {execution_time:.6f} sec")
    assert output == result


@pytest.mark.parametrize("a,b,result", [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)])
def test_half_adder_carry(a, b, result):
    start_time = time.time()
    output = half_adder_carry(a, b)
    end_time = time.time()
    execution_time = end_time - start_time

    log_message(f"TEST: half_adder_carry({a}, {b}) -> Expected: {result}, Got: {output}, Execution Time: {execution_time:.6f} sec")
    assert output == result
