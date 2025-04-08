import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue

@cocotb.test()
async def test_alu_operations(dut):
    """Test ALU operations for various ALU_Sel cases"""

    # Define test cases as (A, B, ALU_Sel, expected ALU_Out, expected CarryOut)
    test_vectors = [
        (0b0011, 0b0001, 0b000, 0b0110, 0),  # A + B = 3 + 1 = 4
        (0b1111, 0b0001, 0b000, 0b0000, 1),  # 15 + 1 = 16 -> overflow CarryOut
        (0b0100, 0b0001, 0b001, 0b0011, 0),  # A - B = 4 - 1 = 3
        (0b0011, 0b0101, 0b010, 0b0001, 0),  # A & B = 3 & 5 = 1
        (0b0011, 0b0101, 0b011, 0b0111, 0),  # A | B = 3 | 5 = 7
        (0b0011, 0b0101, 0b100, 0b0110, 0),  # A ^ B = 3 ^ 5 = 6
        (0b1010, 0b0000, 0b101, 0b0101, 0),  # ~A = ~10 = 5 (4-bit)
        (0b0011, 0b0000, 0b110, 0b0110, 0),  # A << 1 = 3 << 1 = 6
        (0b1010, 0b0000, 0b111, 0b0101, 0),  # A >> 1 = 10 >> 1 = 5
    ]

    for A, B, sel, expected_out, expected_carry in test_vectors:
        dut.A.value = A
        dut.B.value = B
        dut.ALU_Sel.value = sel

        await Timer(10, units="ns")

        assert dut.ALU_Out.value == expected_out, f"ALU_Out mismatch for A={A:04b}, B={B:04b}, Sel={sel:03b}"
        assert dut.CarryOut.value == expected_carry, f"CarryOut mismatch for A={A:04b}, B={B:04b}, Sel={sel:03b}"
