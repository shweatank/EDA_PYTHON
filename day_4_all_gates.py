from myhdl import *

def and_gate(a,b,c):
    @always_comb
    def logic():
        c.next = a & b
    return logic

def NAND_Gate(a,b,c):
    @always_comb
    def logic():
        c.next = not(a & b)
    return logic

def Nor_Gate(a,b,c):
    @always_comb
    def logic():
        c.next = not(a | b)
    return logic

def not_gate(a,c):
    @always_comb
    def logic():
        c.next = ~a & 1
    return logic

def or_gate(a,b,c):
    @always_comb
    def logic():
        c.next = a | b
    return logic

def simulate_all_gates():
    a, b, c, d, e = [Signal(bool(0)) for _ in range(5)]

    # Instantiate all gates
    and_inst = and_gate(a, b, c)
    nand_inst = NAND_Gate(a, b, d)
    nor_inst = Nor_Gate(a, b, e)
    not_inst = not_gate(a, c)
    or_inst = or_gate(a, b, c)

    @instance
    def stimulus():
        print("a b | AND | NAND | NOR | NOT | OR")
        print("----------------------------------")
        for i in range(2):
            for j in range(2):
                a.next, b.next = i, j
                yield delay(10)
                print(f"{int(a)} {int(b)} | {int(c)} | {int(d)} | {int(e)} | {int(c)} | {int(c)}")

    return and_inst, nand_inst, nor_inst, not_inst, or_inst, stimulus

def test():
    tb = traceSignals(simulate_all_gates)
    sim = Simulation(tb)
    sim.run()
    print("VCD file generated as 'merged_gates.vcd'.")

test()
