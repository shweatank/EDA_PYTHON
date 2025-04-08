import cocotb
from cocotb.triggers import Timer
from cocotb.result import TestSuccess
import csv
from pathlib import Path
from datetime import datetime

# Initialize results directory
RESULTS_DIR = Path("results")
RESULTS_DIR.mkdir(exist_ok=True)
RESULTS_CSV = RESULTS_DIR/"test_results.csv"

def log_test_result(dut, test_case):
    """Log individual test case results"""
    header = not RESULTS_CSV.exists()
    with open(RESULTS_CSV, 'a', newline='') as f:
        writer = csv.writer(f)
        if header:
            writer.writerow(["Timestamp", "Test", "Input", "Expected", "Actual", "Status"])
        writer.writerow([
            datetime.now().isoformat(),
            str(dut._name),
            str(test_case[0]),
            str(test_case[1]),
            str(int(dut.Y.value)),
            "PASS" if dut.Y.value == test_case[1] else "FAIL"
        ])

@cocotb.test()
async def test_not_gate(dut):
    """Test NOT gate functionality"""
    test_cases = [(0, 1), (1, 0)]
    
    for test_input, expected in test_cases:
        dut.A.value = test_input
        await Timer(10, units="ns")
        
        # Log and verify results
        log_test_result(dut, (test_input, expected))
        assert dut.Y.value == expected, f"Failed at A={test_input}"
    
    dut._log.info("All test cases passed")
    raise TestSuccess("NOT gate verified")