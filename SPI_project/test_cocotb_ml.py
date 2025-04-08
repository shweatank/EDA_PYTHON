import cocotb
from cocotb.triggers import RisingEdge, Timer    #synchronize with the DUT (Device Under Test) clock.
import random
import numpy as np
from sklearn.tree import DecisionTreeClassifier

@cocotb.test()
async def spi_ml_test(dut):
    """SPI Master Test with ML Model Training (with live accuracy logging)"""

    async def clock_gen():
        while True:                #one full clock cycle is 10ns
            dut.clk.value = 0      #clock set to 0
            await Timer(5, units="ns")
            dut.clk.value = 1
            await Timer(5, units="ns")

    cocotb.start_soon(clock_gen())

    X = []                 #input feature for the model
    Y = []                  #target  (done)
    skipped_samples = 0    #how many samples are skipped due to unknown values

    for i in range(50):  # 50 test cycles
        # Random 8-bit input
        data = random.randint(0, 255)

        # Reset and apply inputs
        dut.start.value = 0
        dut.data_in.value = data
        dut.done.value = 0

        await RisingEdge(dut.clk)
        dut.start.value = 1             #asserting the clock signal to 1 for proper synchronization
        await RisingEdge(dut.clk)
        dut.start.value = 0             #de-assert  the start to 0,here i clock cycle is completed and return to 0

        # Observe for 40 clock cycles
        for _ in range(40): #40 cycles is a buffer to give the SPI Master enough time to complete the entire transaction, including overhead.
            await RisingEdge(dut.clk)

            # Skip if any value is 'x' or 'z'
            signals = [dut.data_in, dut.mosi, dut.sclk, dut.done]
            if not all(sig.value.is_resolvable for sig in signals):   # checks if all the signal values are "resolvable"
                skipped_samples += 1
                continue

            features = [
                int(dut.data_in.value),
                int(dut.mosi.value),
                int(dut.sclk.value),
                int(dut.done.value)
            ]
            X.append(features)
            Y.append(int(dut.done.value))

        # Check if transfer completed
        if dut.done.value.is_resolvable and int(dut.done.value) == 0:
            raise cocotb.result.TestFailure(f"SPI transfer failed for data {data:#02x}")

        # Train model and print accuracy after each round
        if len(X) > 0:
            model = DecisionTreeClassifier()
            model.fit(np.array(X), np.array(Y))
            acc = model.score(X, Y)
            cocotb.log.info(f"[{i+1}/50] ML Model Accuracy after transfer {i+1}: {acc:.4f}")

    cocotb.log.info(f"Simulation completed with {skipped_samples} skipped samples due to unresolvable values.")