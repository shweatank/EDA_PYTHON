import cocotb
from cocotb.triggers import RisingEdge, Timer
import csv
import os

@cocotb.test()
async def spi_transfer_csv_tests(dut):
    # Clock generation coroutine
    async def clock_gen():
        while True:
            dut.clk.value = 0
            await Timer(5, units="ns")
            dut.clk.value = 1
            await Timer(5, units="ns")

    # Start clock
    cocotb.start_soon(clock_gen())

    # Path to the CSV file
    test_cases_path = os.path.join(os.path.dirname(__file__), "spi_testcases.csv")

    with open(test_cases_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for i, row in enumerate(reader):
            data_in = int(row["data_in"])
            expected_mosi = row["expected_mosi"]

            # Reset DUT signals
            dut.start.value = 0
            dut.data_in.value = data_in
            dut.done.value = 0

            # Wait a few clock cycles
            for _ in range(2):
                await RisingEdge(dut.clk)

            # Start transmission
            dut.start.value = 1
            await RisingEdge(dut.clk)
            dut.start.value = 0

            bits_captured = ""

            # Monitor mosi line for 8 bits
            for _ in range(16):  # 8 bits with toggling sclk (2x per bit)
                await RisingEdge(dut.clk)
                if int(dut.sclk.value):
                    bits_captured += str(int(dut.mosi.value))

            await RisingEdge(dut.clk)

            assert dut.done.value == 1, f"Test case {i+1}: 'done' signal not set!"
            assert bits_captured.startswith(expected_mosi), f"Test case {i+1}: Expected MOSI={expected_mosi}, got {bits_captured}"
            cocotb.log.info(f"✅ Test case {i+1} passed with data_in={data_in:#04x} -> MOSI={bits_captured}")
