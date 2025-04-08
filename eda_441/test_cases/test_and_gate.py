# test_cases/test_and_gate.py
import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_and_gate(dut):
    """Test simple AND gate"""

    test_vectors = [
        (0, 0, 0),
        (0, 1, 0),
        (1, 0, 0),
        (1, 1, 1),
    ]

    for a, b, expected in test_vectors:
        dut.A.value = a
        dut.B.value = b

        await Timer(5, units='ns')

        assert dut.Y.value == expected, (
            f"Failed: A={a}, B={b} => Y={int(dut.Y.value)} (Expected {expected})"
        )
