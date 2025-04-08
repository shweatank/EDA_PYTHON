import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure

@cocotb.test()
async def test_and_gate(dut):
    """Test for AND gate"""

    for a in [0, 1]:
        for b in [0, 1]:
            dut.a.value = a
            dut.b.value = b
            await Timer(1, units='ns')
            expected = a & b
            assert dut.c.value == expected, f"AND gate failed: {a} & {b} = {dut.c.value}, expected {expected}"
