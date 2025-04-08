import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestFailure


@cocotb.test()
async def test_nor_gate(dut):
    """Test OR gate functionality"""
    for a in [0, 1]:
        for b in [0, 1]:
            dut.a.value = a
            dut.b.value = b
            await Timer(1, units='ns')
            expected = int(not(a | b))
            assert dut.y.value == expected, f"OR Gate Failed: {a} | {b} = {int(dut.y.value)} (Expected: {expected})"
