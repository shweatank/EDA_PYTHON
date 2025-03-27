import time
import pytest

LOG_FILE = "half_adder.log"

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

# Half Adder Functions
def half_adder_sum(a, b):
    return a ^ b  # XOR operation for sum

def half_adder_carry(a, b):
    return a & b  # AND operation for carry

@pytest.mark.parametrize("a, b, expected_sum, expected_carry", [
    (0, 0, 0, 0),
    (0, 1, 1, 0),
    (1, 0, 1, 0),
    (1, 1, 0, 1)
])
def test_half_adder(a, b, expected_sum, expected_carry):
    """Test cases for Half Adder (Sum and Carry)."""
    sum_result, sum_time = measure_time(half_adder_sum, a, b)
    carry_result, carry_time = measure_time(half_adder_carry, a, b)

    message_sum = f"SUM({a}, {b}) -> Output: {sum_result}, Expected: {expected_sum}, Time: {sum_time:.10f} sec"
    message_carry = f"CARRY({a}, {b}) -> Output: {carry_result}, Expected: {expected_carry}, Time: {carry_time:.10f} sec"

    print(message_sum)
    print(message_carry)

    log_result(message_sum)
    log_result(message_carry)

    assert sum_result == expected_sum
    assert carry_result == expected_carry
