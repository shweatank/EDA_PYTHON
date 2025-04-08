import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_nand_gate(dut):
    """Test NAND gate functionality"""
    test_cases = [
        (0, 0, 1),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0)
    ]

    for a, b, expected in test_cases:
        dut.A.value = a
        dut.B.value = b
        await Timer(10, units="ns")
        assert dut.Y.value == expected, f"NAND Failed at A={a}, B={b}, Got Y={dut.Y.value}"
