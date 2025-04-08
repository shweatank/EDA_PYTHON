from myhdl import *
def or_Gate(a,b,c):
    @always_comb
    def logic():
        c.next=a | b
    return logic

#simulation
def simulate_or_gate():
    a,b,c=[Signal(bool(0)) for _ in range(3)]
    def bench():
        or_inst=or_Gate(a,b,c)
        @instance
        def stimulus():
            print("a b | c")
            print("-------")
            for i in range(2):
                for j in range(2):
                    a.next, b.next=i,j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(c)}')
        return or_inst,stimulus
    #generate vcd
    tb=traceSignals(bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as 'or_gate.vcd.'")
#run
def test():
    simulate_or_gate()
test()