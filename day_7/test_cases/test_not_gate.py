import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_not_gate(dut):
    test_cases = [
        (0, 1),
        (1, 0)
    ]

    for a, expected in test_cases:
        dut.A.value = a
        await Timer(10, units="ns")
        assert dut.Y.value == expected, f"Failed at A={a}"