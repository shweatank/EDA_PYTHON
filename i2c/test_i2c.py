import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer

@cocotb.test()
async def i2c_basic_write(dut):
    # Start clock
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Initialize all inputs
    dut.start.value = 0
    dut.addr.value = 0
    dut.data.value = 0
    await Timer(20, units="ns")  # Reset period

    # Start I2C transaction
    dut.addr.value = 0x50
    dut.data.value = 0xA5
    await RisingEdge(dut.clk)
    dut.start.value = 1
    await RisingEdge(dut.clk)
    dut.start.value = 0

    # Wait for transaction to complete (~20 clock cycles)
    for _ in range(50):
        await RisingEdge(dut.clk)
        print(f"SCL: {dut.scl.value}, SDA: {dut.sda.value}")  # Debug

    # Final check
    assert dut.scl.value == 1, "SCL should be high after transaction"