from myhdl import *

def HALF_ADDER(a, b, sum, carry):
    @always_comb
    def logic():
        sum.next = a ^ b
        carry.next = a and b
    
    return logic

def simulate_and_gate():
    a, b, sum, carry = [Signal(bool(0)) for _ in range(4)]

    def half_adder_bench():
        half_adder_inst = HALF_ADDER(a, b, sum, carry)

        @instance
        def stimulus():
            print("a b | sum carry")
            print("----------------------------")
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)
                    print(f"{int(a)} {int(b)} | {int(sum)} {int(carry)}")
        
        return half_adder_inst, stimulus
    
    tb = traceSignals(half_adder_bench)
    sim = Simulation(tb)
    sim.run()


def test():
    simulate_and_gate()
test()