from myhdl import *

def OR_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = a | b
    
    return logic

def simulate_and_gate():
    a, b, c = [Signal(bool(0)) for _ in range(3)]

    def or_bench():
        or_inst = OR_Gate(a, b, c)

        @instance
        def stimulus():
            print("a b | c")
            print("----------------------------")
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)
                    print(f"{int(a)} {int(b)} | {int(c)}")
        
        return or_inst, stimulus
    
    tb = traceSignals(or_bench)
    sim = Simulation(tb)
    sim.run()


def test():
    simulate_and_gate()
test()