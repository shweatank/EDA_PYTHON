# import cocotb
# from cocotb.triggers import Timer

# @cocotb.test()
# async def test_nand_gate(dut):
#     """Test NAND gate functionality"""
#     test_cases = [
#         (0, 0, 1),
#         (0, 1, 1),
#         (1, 0, 1),
#         (1, 1, 0)
#     ]

#     for a, b, expected in test_cases:
#         dut.A.value = a
#         dut.B.value = b
#         await Timer(10, units='ns')
#         assert int(dut.Y.value) == expected, f"Failed for A={a}, B={b}. Expected={expected}, Got={int(dut.Y.value)}"

import cocotb
from cocotb.triggers import Timer
import os


@cocotb.test()
async def test_nand_gate(dut):
    """Test NAND gate and generate a VCD waveform."""

    # Enable VCD dump (Optional: Change file path)
    os.environ["WAVES"] = "1"

    test_cases = [
        (0, 0, 1),
        (0, 1, 1),
        (1, 0, 1),
        (1, 1, 0),
    ]

    for a, b, expected in test_cases:
        dut.A.value = a
        dut.B.value = b
        await Timer(10, units="ns")

        if dut.Y.value != expected:
            raise cocotb.result.TestFailure(
                f"Failed: A={a}, B={b}, Expected={expected}, Got={int(dut.Y.value)}"
            )

    print("✅ Test Passed!")