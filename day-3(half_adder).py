from google.protobuf.internal.test_bad_identifiers_pb2 import message
from myhdl import *
import logging

logging.basicConfig(
    filename="half_adder_log.txt",
    level=logging.INFO,
    format="%(message)s",
)

def half_adder(a, b, s, c):
    @always_comb
    def logic():
        s.next = a ^ b
        c.next = a and b
    return logic

# Simulation
def simulate_half_adder():
    a, b, s, c = [Signal(bool(0)) for _ in range(4)]  # Create signals

    def bench():
        not_inst = half_adder(a,b,s,c)
        @instance
        def stimulus():
            print("a b | s c")
            logging.info("a  b | s  c")
            print("----------")
            logging.info("--------------")
            for i in range(2):
                a.next = i
                for j in range(2):
                    b.next = j
                    yield delay(10)
                    result = f"{int(a)}  {int(b)} | {int(s)} {int(c)}"
                    print(result)
                    logging.info(result)
        return not_inst, stimulus

    # Generate VCD file for waveform analysis
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()
    print("VCD file generated")

# Run simulation
def test():
    simulate_half_adder()

test()
