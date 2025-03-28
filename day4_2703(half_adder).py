from myhdl import *

# Half Adder Module
def half_adder(a, b, sum, carry):
    """
    Implements a simple half adder.
    a, b -> Inputs
    sum -> Sum Output (XOR)
    carry -> Carry Output (AND)
    """
    @always_comb
    def logic():
        sum.next = a ^ b
        carry.next = a & b
    return logic

# Simulation for Half Adder
def simulate_half_adder():
    # Signals for inputs and outputs
    a, b, sum, carry = [Signal(bool(0)) for _ in range(4)]

    # Testbench definition
    def bench():
        # Instantiate the half adder
        ha_inst = half_adder(a, b, sum, carry)

        @instance
        def stimulus():
            print("a b | sum carry")
            print("----------------")
            for i in range(2):  # Loop through all values of input a
                for j in range(2):  # Loop through all values of input b
                    a.next, b.next = i, j
                    yield delay(10)  # Wait for 10 units of simulation time
                    print(f"{int(a)} {int(b)} | {int(sum)}   {int(carry)}")
            raise StopSimulation()

        return ha_inst, stimulus

    # Generate VCD (waveform) file for analysis
    tb = traceSignals(bench)  # Generate trace signals
    sim = Simulation(tb)      # Create a simulation object
    sim.run()                 # Run the simulation
    print("VCD file generated as 'half_adder.vcd'.")

# Run the simulation
if __name__ == "__main__":
    simulate_half_adder()
