from myhdl import *
def half_adder_gate(a,b,s,c):
    """
    Basic and gate:Implements a simple two-input and gate.
    a,b->Inputs
    c->Output
    """
    @always_comb
    def logic():
        s.next = a ^ b
        c.next= a and b
    return logic

#simulation         
def simulate_half_adder_gate():
    a,b,s,c= [Signal(bool(0)) for _ in range(4)]

    def bench():
        and_inst = half_adder_gate(a,b,s,c)

        @instance
        def stimulus():
            print("a b | s | c")
            print("---------")
            for i in range(2):
                for j in range(2):
                    a.next,b.next = i, j
                    yield delay(10)
                    print(f"{int(a)} {int(b)} | {int(s)} | {int(c)}")

        return and_inst, stimulus

    #Generate VCD File for waveform analysis
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()
    print("VCD file generated as 'half_adder_gate.vcd'.")

#Run simulation
def test():
    simulate_half_adder_gate()
test()
