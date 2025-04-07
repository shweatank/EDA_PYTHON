import cocotb
from cocotb.triggers import Timer
import logging

@cocotb.test()
async def adder_basic_test(dut):
    """Basic test for the 4-bit adder"""

    dut._log.setLevel(logging.INFO)
    test_vectors = [
        (0b0000, 0b0000),
        (0b0011, 0b0101),
        (0b1111, 0b0001),
        (0b1010, 0b1010),
    ]

    for a_val, b_val in test_vectors:
        dut.a.value = a_val
        dut.b.value = b_val
        await Timer(10, units="ns")

        expected = a_val + b_val
        actual = dut.sum.value.integer

        dut._log.info(f"Testing: a={a_val:04b}, b={b_val:04b}, sum={actual:05b}")
        assert actual == expected, f"Adder failed: {a_val}+{b_val} != {actual}"