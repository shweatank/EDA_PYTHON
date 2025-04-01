from myhdl import *

def full_adder(a, b, cin, sum, cout):
    @always_comb
    def logic():
        sum.next = a ^ b ^ cin
        cout.next = ((a ^ b) & cin) | (a & b)
    return logic

def simulate_full_adder():
    a, b, cin, sum, cout = [Signal(bool(0)) for _ in range(5)]
    
    def full_adder_bench():
        fa_inst = full_adder(a, b, cin, sum, cout)
        
        @instance
        def stimulus():
            print("a b cin | sum cout")
            print("----------------")
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        a.next, b.next, cin.next = i, j, k
                        yield delay(10)
                        print(f"{int(a)} {int(b)} {int(cin)} | {int(sum)} {int(cout)}")
        
        return fa_inst, stimulus
    
    tb = traceSignals(full_adder_bench)
    sim = Simulation(tb)
    sim.run()
    print("VCD file generated as 'full_adder.vcd'.")

def test():
    simulate_full_adder()

test()