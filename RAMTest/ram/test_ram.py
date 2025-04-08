"""
Example of a simple testbench for a RAM block
"""
import random

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge, ReadOnly


@cocotb.coroutine
async def write_ram(dut, address, value):
    """This coroutine performs a write of the RAM"""
    await RisingEdge(dut.clk_write)  # Synchronise to the write clock
    dut.address_write.value = address
    dut.data_write.value = value
    dut.write_enable.value = 1
    await RisingEdge(dut.clk_write)
    dut.write_enable.value = 0


@cocotb.coroutine
async def read_ram(dut, address):
    """This coroutine performs a read of the RAM and returns a value"""
    await RisingEdge(dut.clk_read)  # Synchronise to the read clock
    dut.address_read.value = address
    await RisingEdge(dut.clk_read)
    await ReadOnly()
    return int(dut.data_read.value)


@cocotb.test()
async def test_ram(dut):
    """Try writing values into the RAM and reading back"""
    RAM = {}

    # Read the parameters back from the DUT to set up our model
    width = dut.D_WIDTH.value
    depth = 2 ** dut.A_WIDTH.value
    dut._log.info("Found %d entry RAM by %d bits wide" % (depth, width))

    # Set up independent read/write clocks
    cocotb.start_soon(Clock(dut.clk_write, 3200).start())
    cocotb.start_soon(Clock(dut.clk_read, 5000).start())

    dut._log.info("Writing in random values")
    for i in range(depth):
        RAM[i] = int(random.getrandbits(width))
        await write_ram(dut, i, RAM[i])

    dut._log.info("Reading back values and checking")
    for i in range(depth):
        value = await read_ram(dut, i)
        if value != RAM[i]:
            dut._log.error("RAM[%d] expected %d but got %d" % (i, RAM[i], value))
            assert False, "RAM contents incorrect"
    dut._log.info("RAM contents OK")


def test_runner():
    import os
    from cocotb.runner import get_runner

    runner = get_runner(os.getenv("SIM"))
    runner.build(
        verilog_sources=["design.sv"],
        hdl_toplevel="ram",
        always=True,
    )

    runner.test(hdl_toplevel="ram", test_module="testbench")


if __name__ == "__main__":
    test_runner()
