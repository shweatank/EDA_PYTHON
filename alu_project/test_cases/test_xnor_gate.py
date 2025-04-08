import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_xnor_gate(dut):
    """Test XNOR gate functionality"""
    test_cases = [
        (0, 0, 1),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 1)
    ]

    for a, b, expected in test_cases:
        dut.A.value = a
        dut.B.value = b
        await Timer(10, units="ns")
        assert dut.Y.value == expected, f"XNOR Failed at A={a}, B={b}, Got Y={int(dut.Y.value)}"
