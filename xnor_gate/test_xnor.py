import cocotb
from cocotb.triggers import Timer
import csv

@cocotb.test()
async def test_xnor_gate(dut):
    """Test OR Gate and generate VCD file"""

    # Enable waveform dumping

    # Load test cases from a CSV file
    with open("truth_table.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        test_vectors = [list(map(int, row)) for row in reader]

    for vector in test_vectors:
        a, b, expected_y = vector

        # Apply inputs
        dut.A.value = a
        dut.B.value = b
        await Timer(5, units="ns")  # Wait for the output to settle

        # Check the output
        assert dut.Y.value == expected_y, f"XNOR Gate failed for A={a}, B={b}"

    print("✅ XNOR Gate Test Passed!")
