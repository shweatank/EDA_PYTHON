from myhdl import *
def not_gate(a,c):
    """
    Basic and gate:Implements a simple two-input and gate.
    a,b->Inputs
    c->Output
    """
    @always_comb
    def logic():
        c.next = ~a & 1
    return logic

#simulation
def simulate_not_gate():
    a,c = [Signal(bool(0)) for _ in range(2)]

    def bench():
        and_inst = not_gate(a,c)

        @instance
        def stimulus():
            print("a | c")
            print("---------")
            for i in range(2):

                a.next = i
                yield delay(10)
                print(f"{int(a)}  | {int(c)}")

        return and_inst, stimulus

    #Generate VCD File for waveform analysis
    tb = traceSignals(bench)           # traceSignal() is a sdl method
    sim = Simulation(tb)     # it is used to create VCD file.
    sim.run()
    print("VCD file generated as 'not_gate.vcd'.")

#Run simulation
def test():
    simulate_not_gate()
test()