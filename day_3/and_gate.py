from myhdl import *

def AND_Gate(a,b,c):
    @always_comb
    def logic():
        c.next=a & b
    return logic


def simulate_and_logic():
    a,b,c=[Signal(bool(0)) for _ in range(3)]

    def and_bench():
        and_inst=AND_Gate(a,b,c)

        @instance
        def stimulus():
            print('a b | c')
            print('----------------------')
            for i in range(2):
                for j in range(2):
                    a.next, b.next=i, j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(c)}')
    
        return and_inst, stimulus
    
    tb= traceSignals(and_bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as 'and_bench.vcd'.")

def test():
    simulate_and_logic()

test()


