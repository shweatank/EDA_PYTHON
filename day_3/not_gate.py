from myhdl import *

def NOT_Gate(a,b):
    @always_comb
    def logic():
        b.next=int(not a)
    return logic


def simulate_not_logic():
    a,b=[Signal(bool(0)) for _ in range(2)]

    def not_bench():
        not_inst=NOT_Gate(a,b)

        @instance
        def stimulus():
            print('a | b')
            print('----------------------')
            for i in range(2):
                
                a.next=i
                yield delay(10)
                print(f'{int(a)} | {int(b)}')
    
        return not_inst, stimulus
    
    tb= traceSignals(not_bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as 'not_bench.vcd'.")

def test():
    simulate_not_logic()

test()