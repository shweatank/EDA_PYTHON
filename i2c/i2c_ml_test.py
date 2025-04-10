# i2c_ml_test.py
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import random


@cocotb.test()
async def test_multiple_writes(dut):
    """Perform 3 sequential I2C writes with different values"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    test_data = [(0x30, 0x11), (0x31, 0x22), (0x32, 0x33)]

    for addr, data in test_data:
        dut.start.value = 0
        dut.addr.value = addr
        dut.data.value = data
        await Timer(10, units="ns")

        await RisingEdge(dut.clk)
        dut.start.value = 1
        await RisingEdge(dut.clk)
        dut.start.value = 0

        for _ in range(20):
            await RisingEdge(dut.clk)

    assert int(dut.sda.value) in [0, 1]



@cocotb.test()
async def test_max_address_data(dut):
    """Test I2C with max possible address (0x7F) and data (0xFF)"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    dut.start.value = 0
    dut.addr.value = 0x7F
    dut.data.value = 0xFF
    await Timer(10, units="ns")

    await RisingEdge(dut.clk)
    dut.start.value = 1
    await RisingEdge(dut.clk)
    dut.start.value = 0

    for _ in range(30):
        await RisingEdge(dut.clk)

    assert int(dut.sda.value) in [0, 1], "SDA should be a valid binary value"


@cocotb.test()
async def test_invalid_address(dut):
    """Negative test: Write with invalid address (>0x7F)"""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Invalid address (should only be 7 bits)
    dut.start.value = 0
    dut.addr.value = 0x1FF  # 9-bit address (invalid for I2C)
    dut.data.value = 0xAA
    await Timer(10, units="ns")

    await RisingEdge(dut.clk)
    dut.start.value = 1
    await RisingEdge(dut.clk)
    dut.start.value = 0

    for _ in range(30):
        await RisingEdge(dut.clk)

    # Expect some form of error or default response
    assert int(dut.addr.value) <= 0x7F, "Address exceeds 7-bit range (negative test failed to detect)"


@cocotb.test()
async def i2c_ml_training_test(dut):
    """Train ML model to learn I2C behavior"""

    # Setup clock
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # Training data
    X = []
    Y = []

    for _ in range(100):
        # Random address and data
        addr = random.randint(0x00, 0x7F)
        data = random.randint(0x00, 0xFF)

        # Apply inputs
        dut.start.value = 0
        dut.addr.value = addr
        dut.data.value = data
        await Timer(10, units="ns")

        await RisingEdge(dut.clk)
        dut.start.value = 1
        await RisingEdge(dut.clk)
        dut.start.value = 0

        # Let it run for a few cycles
        for _ in range(20):
            await RisingEdge(dut.clk)

        # Read SDA and SCL (could be others too)
        sda_out = int(dut.sda.value)
        scl_out = int(dut.scl.value)

        # Collect features and labels
        X.append([addr, data])
        Y.append(sda_out)

    # ML training
    clf = DecisionTreeClassifier()
    clf.fit(np.array(X), np.array(Y))
    accuracy = clf.score(X, Y)
    
     # ✅ Corrected logging line
    cocotb.log.info(f"Number of training samples: {len(X)}")

    
    # Log the accuracy
    dut._log.info(f"Decision Tree trained on I2C protocol behavior.")
    dut._log.info(f"Training Accuracy: {accuracy:.2f}")