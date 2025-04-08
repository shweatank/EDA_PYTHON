import cocotb
from cocotb.triggers import Timer
import random

@cocotb.test()
async def test_not_gate(dut):
    """Test NOT gate behavior"""

    for i in range(2):
        dut.a.value = i
        await Timer(1, units='ns')
        expected = int(not i)
        assert dut.y.value == expected, f"Failed: a={i}, expected y={expected}, got y={dut.y.value}"
