from myhdl import *

def NOT_Gate(a,b):

    @always_comb
    def logic():
        b.next=not(a)
    return logic
#simulation
def simulate_and_gate():
    a,b=[Signal(bool(0)) for _ in range(2)]

    def bench():
        and_inst=NOT_Gate(a,b)

        @instance
        def stimulus():
            print("a | b")
            print("----------")
            for i in range(2):
                a.next=i
                yield delay(10)
                print(f"{int(a)} | {int(b)}")
        return and_inst,stimulus
    #Generate vcd file for waveform analysis
    tb=traceSignals(bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as 'not_gate.vcd'.")

#Run simulation
def test():
    simulate_and_gate()
test()
