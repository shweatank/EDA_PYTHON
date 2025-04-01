from myhdl import *

def full_adder(a,b,cin,s,c):
    @always_comb
    def logic():
        s.next=a ^ b ^ cin
        c.next=(a & b) | (a & cin) | (b & cin)
    return logic


def simulate_fulladder_logic():
    a,b,cin,s,c=[Signal(bool(0)) for _ in range(5)]

    def fulladder_bench():
        fulladder_inst=full_adder(a,b,cin,s,c)

        @instance
        def stimulus():
            print('a b cin | s c')
            print('------------------------')
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        a.next, b.next ,cin.next=i, j ,k
                        yield delay(10)
                        print(f'{int(a)} {int(b)} {int(cin)} | {int(s)} {int(c)}')
        
        return fulladder_inst, stimulus
    
    tb= traceSignals(fulladder_bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as 'halfadder_bench.vcd'.")

def test():
    simulate_fulladder_logic()

test()