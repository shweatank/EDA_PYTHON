import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_or_gate(dut):
    test_cases = [
        (0, 0, 0),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 1)
    ]

    for a, b, expected in test_cases:
        dut.A.value = a
        dut.B.value = b
        await Timer(10, units="ns")
        assert dut.Y.value == expected, f"Failed at A={a}, B={b}"