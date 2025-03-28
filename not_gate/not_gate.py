from myhdl import *

def NOT_Gate(a, c):
    @always_comb
    def logic():
        c.next = 1 if not a else 0
    
    return logic

def simulate_and_gate():
    a, c = [Signal(bool(0)) for _ in range(2)]

    def not_bench():
        not_inst = NOT_Gate(a, c)

        @instance
        def stimulus():
            print("a | c")
            print("----------------------------")
            for i in range(2):
                a.next = i
                yield delay(10)
                print(f"{int(a)} | {int(c)}")
        
        return not_inst, stimulus
    
    tb = traceSignals(not_bench)
    sim = Simulation(tb)
    sim.run()


def test():
    simulate_and_gate()
test()