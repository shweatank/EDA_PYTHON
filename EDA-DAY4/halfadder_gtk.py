from myhdl import *

def halfadder_Gate(a,b,c,d):

    @always_comb
    def logic():
        c.next,d.next=a^b,a&b
    return logic
#simulation
def simulate_and_gate():
    a,b,c,d=[Signal(bool(0)) for _ in range(4)]

    def bench():
        halfadder_inst=halfadder_Gate(a,b,c,d)

        @instance
        def stimulus():
            print("a | b | c | d")
            print("----------")
            for i in range(2):
                for j in range(2):
                    a.next,b.next=i,j
                    yield delay(10)
                    print(f"{int(a)} | {int(b)} | {int(c)} | {int(d)}")
        return halfadder_inst,stimulus
    #Generate vcd file for waveform analysis
    tb=traceSignals(bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as 'halfadder_gate.vcd'.")

#Run simulation
def test():
    simulate_and_gate()
test()
