from myhdl import *
import time


def AND_Gate(a, b, c):
    """MyHDL model of an AND gate"""

    @always_comb
    def logic():
        c.next = a & b

    return logic


def OR_Gate(a, b, c):
    """MyHDL model of an OR gate"""

    @always_comb
    def logic():
        c.next = a | b

    return logic


def NAND_Gate(a, b, c):
    """MyHDL model of a NAND gate"""

    @always_comb
    def logic():
        c.next = not (a & b)

    return logic


def NOR_Gate(a, b, c):
    """MyHDL model of a NOR gate"""

    @always_comb
    def logic():
        c.next = not (a | b)

    return logic


def XOR_Gate(a, b, c):
    """MyHDL model of an XOR gate"""

    @always_comb
    def logic():
        c.next = a ^ b

    return logic


def XNOR_Gate(a, b, c):
    """MyHDL model of an XNOR gate"""

    @always_comb
    def logic():
        c.next = not (a ^ b)

    return logic


# Function to get timestamp for logging
def get_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]


# Simulation function
def simulate_gates():
    """Simulates all logic gates and logs the results to a file"""

    log_filename = "logic_gates_simulation.txt"

    with open(log_filename, "a") as log_file:

        def log_message(level, message):
            """Write logs in the required format"""
            log_file.write(f"{get_timestamp()} - {level} - {message}\n")

        # Start total execution time measurement
        total_start_time = time.time()

        # Define input and output signals
        a, b = [Signal(bool(0)) for _ in range(2)]
        and_out, or_out, nand_out, nor_out, xor_out, xnor_out = [Signal(bool(0)) for _ in range(6)]

        def bench():
            # Instantiate all gates
            and_inst = AND_Gate(a, b, and_out)
            or_inst = OR_Gate(a, b, or_out)
            nand_inst = NAND_Gate(a, b, nand_out)
            nor_inst = NOR_Gate(a, b, nor_out)
            xor_inst = XOR_Gate(a, b, xor_out)
            xnor_inst = XNOR_Gate(a, b, xnor_out)

            @instance
            def stimulus():
                log_message("INFO", "Simulation started.")
                start_time = time.time()  # Start time for simulation

                print("a b | AND OR NAND NOR XOR XNOR")
                print("---------------------------------")
                log_file.write("a b | AND OR NAND NOR XOR XNOR\n")
                log_file.write("---------------------------------\n")

                for i in range(2):
                    for j in range(2):
                        cycle_start_time = time.time()
                        a.next, b.next = i, j
                        yield delay(10)
                        cycle_end_time = time.time()
                        cycle_execution_time = cycle_end_time - cycle_start_time  # Compute time taken

                        result = f"{int(a)} {int(b)} |  {int(and_out)}   {int(or_out)}   {int(nand_out)}    {int(nor_out)}    {int(xor_out)}    {int(xnor_out)}"
                        print(result)
                        log_message("INFO",
                                    f"Inputs: A={int(a)}, B={int(b)} -> Outputs: AND={int(and_out)}, OR={int(or_out)}, NAND={int(nand_out)}, NOR={int(nor_out)}, XOR={int(xor_out)}, XNOR={int(xnor_out)} (Execution Time: {cycle_execution_time:.6f} sec)")
                        log_file.write(result + f"  | Execution Time: {cycle_execution_time:.6f} sec\n")

                end_time = time.time()
                execution_time = end_time - start_time
                log_message("INFO", f"Simulation completed. Execution time: {execution_time:.6f} seconds")
                log_file.write(f"\nExecution Time: {execution_time:.6f} seconds\n")

            return and_inst, or_inst, nand_inst, nor_inst, xor_inst, xnor_inst, stimulus

        tb = traceSignals(bench)
        sim = Simulation(tb)
        sim.run()

        # End total execution time measurement
        total_end_time = time.time()
        total_execution_time = total_end_time - total_start_time

        log_message("INFO", f"Total execution time for the entire program: {total_execution_time:.6f} seconds")
        log_file.write(f"\nTotal Execution Time: {total_execution_time:.6f} seconds\n")

        log_message("INFO", "VCD file generated as 'logic_gates.vcd'.")
        print("VCD file generated as 'logic_gates.vcd'.")


# Run the simulation
def test():
    simulate_gates()


test()
