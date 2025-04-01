from myhdl import *

def half_adder(a,b,s,c):
    @always_comb
    def logic():
        s.next=a ^ b
        c.next=a & b
    return logic


def simulate_halfadder_logic():
    a,b,s,c=[Signal(bool(0)) for _ in range(4)]

    def halfadder_bench():
        halfadder_inst=half_adder(a,b,s,c)

        @instance
        def stimulus():
            print('a b | s c')
            print('----------------------')
            for i in range(2):
                for j in range(2):
                    a.next, b.next=i, j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(s)} {int(c)}')
    
        return halfadder_inst, stimulus
    
    tb= traceSignals(halfadder_bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as 'halfadder_bench.vcd'.")

def test():
    simulate_halfadder_logic()

test()