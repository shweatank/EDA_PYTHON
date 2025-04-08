import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.result import TestFailure


@cocotb.test()
async def uart_transmit_test(dut):
    """Test UART transmission"""

    # Generate clock
    async def clock_gen():
        while True:
            dut.clk.value = 0
            await Timer(5, units="ns")
            dut.clk.value = 1
            await Timer(5, units="ns")

    cocotb.start_soon(clock_gen())

    dut.start.value = 0
    dut.data.value = 0x55  # test pattern

    await Timer(10, units="ns")
    dut.start.value = 1
    await RisingEdge(dut.clk)
    dut.start.value = 0

    # Wait for transmission to complete
    timeout = 1000
    cycles = 0
    while not dut.done.value:
        await RisingEdge(dut.clk)
        cycles += 1
        if cycles > timeout:
            raise TestFailure("Timeout: UART transmission did not complete.")

    dut._log.info("Transmission completed.")

    if not dut.done.value:
        raise TestFailure(" CASE 1: 'done' should be high after transmission but is low.")

    expected_data = 0x55  # incorrect expected data (should fail, we sent 0x55)
    if int(dut.data.value) != expected_data:
        raise TestFailure(
            f" CASE 2: Expected transmitted data to be {hex(expected_data)}, but got {hex(int(dut.data.value))}"
        )