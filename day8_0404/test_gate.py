import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def run_gate_test(dut):
    for _ in range(5):
        A = random.randint(0, 1)
        B = random.randint(0, 1)

        dut.A.value = A
        dut.B.value = B

        await Timer(2, units='ns')

        # Compute expected value based on DUT name
        dut_name = dut._name
        if dut_name == "nand_gate":
            expected = ~(A & B) & 1
        elif dut_name == "nor_gate":
            expected = ~(A | B) & 1
        elif dut_name == "xor_gate":
            expected = (A ^ B) & 1
        else:
            raise ValueError(f"Unknown gate: {dut_name}")

        assert dut.Y.value == expected, f"Failed: {A=}, {B=}, got {dut.Y.value}, expected {expected}"
