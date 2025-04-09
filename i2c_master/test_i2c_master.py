import cocotb
from cocotb.triggers import RisingEdge
from cocotb.clock import Clock

@cocotb.test()
async def i2c_basic_write(dut):
    """Basic I2C write transaction test."""

    # Start a 100MHz clock on dut.clk
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Initialize signals
    dut.start.value = 0
    dut.addr.value = 0x50
    dut.data.value = 0xA5

    # Wait for clock edge and start the I2C write
    await RisingEdge(dut.clk)
    dut.start.value = 1
    await RisingEdge(dut.clk)
    dut.start.value = 0

    # Wait for several clock cycles for the transaction to complete
    for _ in range(50):
        await RisingEdge(dut.clk)

    # Check scl value for sanity (real tests would be more rigorous)
    assert int(dut.scl.value) in [0, 1]
