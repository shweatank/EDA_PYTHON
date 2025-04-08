from myhdl import *

def AND_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = a & b
    return logic

# Simulation
def simulate_and_gate():
    a, b, c = [Signal(bool(0)) for _ in range(3)]

    def bench():
        and_inst = AND_Gate(a, b, c)

        @instance
        def stimulus():
            print("a b | c")
            print("-------")
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(c)}')
            raise StopSimulation

        return and_inst, stimulus

    # VCD generation with custom name
    tb = traceSignals(bench)  # ❗️No `name` keyword here
    sim = Simulation(tb)
    sim.run()

# Run
def test():
    simulate_and_gate()

test()
