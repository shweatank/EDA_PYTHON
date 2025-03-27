from myhdl import *
import time


def FullAdder(A, B, Cin, Sum, Cout):
    """ Full Adder using MyHDL """

    @always_comb
    def logic():
        Sum.next = A ^ B ^ Cin
        Cout.next = (A & B) | (Cin & (A ^ B))

    return logic


# Function to get timestamp for logging
def get_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]  


# Simulation function
def simulate_full_adder():

    log_filename = "full_adder_simulation.txt"

    with open(log_filename, "a") as log_file:  

        def log_message(level, message):
            """Write logs in the required format"""
            log_file.write(f"{get_timestamp()} - {level} - {message}\n")

        A, B, Cin = [Signal(bool(0)) for _ in range(3)]
        Sum, Cout = [Signal(bool(0)) for _ in range(2)]

        def bench():
            fa_inst = FullAdder(A, B, Cin, Sum, Cout)

            @instance
            def stimulus():
                log_message("INFO", "Simulation started.")
                start_time = time.time()

                print("A B Cin | Sum Cout")
                print("-----------------")
                log_file.write("A B Cin | Sum Cout\n")
                log_file.write("-----------------\n")

                for i in range(2):
                    for j in range(2):
                        for k in range(2):
                            A.next, B.next, Cin.next = i, j, k
                            yield delay(10)
                            result = f"{int(A)} {int(B)}  {int(Cin)}   |  {int(Sum)}   {int(Cout)}"
                            print(result)
                            log_message("INFO",
                                        f"Inputs: A={int(A)}, B={int(B)}, Cin={int(Cin)} -> Sum={int(Sum)}, Cout={int(Cout)}")
                            log_file.write(result + "\n")

                end_time = time.time()
                execution_time = end_time - start_time
                log_message("INFO", f"Simulation completed. Execution time: {execution_time:.6f} seconds")
                log_file.write(f"\nExecution Time: {execution_time:.6f} seconds\n")

            return fa_inst, stimulus

        tb = traceSignals(bench)
        sim = Simulation(tb)
        sim.run()

        log_message("INFO", "VCD file generated as 'full_adder.vcd'.")
        print("VCD file generated as 'full_adder.vcd'.")


# Run the simulation
def test():
    simulate_full_adder()


test()
