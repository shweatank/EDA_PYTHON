from myhdl import *

def OR_Gate(a,b,c):

    @always_comb
    def logic():
        c.next=a|b
    return logic
#simulation
def simulate_and_gate():
    a,b,c=[Signal(bool(0)) for _ in range(3)]

    def bench():
        and_inst=OR_Gate(a,b,c)

        @instance
        def stimulus():
            print("a b | c")
            print("----------")
            for i in range(2):
                for j in range(2):
                    a.next,b.next=i,j
                    yield delay(10)
                    print(f"{int(a)} {int(b)} | {int(c)}")
        return and_inst,stimulus
    #Generate vcd file for waveform analysis
    tb=traceSignals(bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as 'or_gate.vcd'.")

#Run simulation
def test():
    simulate_and_gate()
test()
