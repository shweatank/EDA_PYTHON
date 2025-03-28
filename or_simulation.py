from myhdl import *
def or_gate(a,b,c):
    """
    Basic and gate:Implements a simple two-input and gate.
    a,b->Inputs
    c->Output
    """
    @always_comb
    def logic():
        c.next = a | b
    return logic

#simulation
def simulate_or_gate():
    a,b,c = [Signal(bool(0)) for _ in range(3)]

    def bench():
        and_inst = or_gate(a,b,c)

        @instance
        def stimulus():
            print("a b | c")
            print("---------")
            for i in range(2):
                for j in range(2):
                    a.next,b.next = i, j
                    yield delay(10)
                    print(f"{int(a)} {int(b)} | {int(c)}")

        return and_inst, stimulus

    #Generate VCD File for waveform analysis
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()
    print("VCD file generated as 'or_gate.vcd'.")

#Run simulation
def test():
    simulate_or_gate()
test()