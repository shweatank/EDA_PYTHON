from myhdl import *

# AND Gate
def and_gate(a, b, c):
    """
    Basic AND gate: Implements a simple two-input AND gate.
    a, b -> Inputs
    c -> Output
    """
    @always_comb
    def logic():
        c.next = a & b
    return logic

# OR Gate
def or_gate(a, b, c):
    """
    Basic OR gate: Implements a simple two-input OR gate.
    a, b -> Inputs
    c -> Output
    """
    @always_comb
    def logic():
        c.next = a or b
    return logic

# NOT Gate (Inverter)
def not_gate(a, b):
    """
    Basic NOT gate: Implements a single-input NOT gate.
    a -> Input
    b -> Output
    """
    @always_comb
    def logic():
        b.next = not a
    return logic

# half adder
def half_adder(a, b,s,c):
    """
    Basic NOT gate: Implements a single-input NOT gate.
    a -> Input
    b -> Output
    """
    @always_comb
    def logic():
        s.next = a ^ b
        c.next=a & b
    return logic



# Simulation for AND, OR, and NOT gates
def simulate_gates():
    a, b, c, d = [Signal(bool(0)) for _ in range(4)]
    c_or, d_or = [Signal(bool(0)) for _ in range(2)]  # OR gate outputs
    s,c = [Signal(bool(0)) for _ in range(2)]

    def bench():
        and_inst = and_gate(a, b, c)
        or_inst = or_gate(a, b, d)
        not_inst = not_gate(a, c_or)
        half_adder_inst=half_adder(a,b,s,c)

        @instance
        def stimulus():
            print("a b | AND c | OR d | NOT c_or   | half_adder: sum  ||  c_out  ")
            print("----------------------------")
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)
                    print(f"{int(a)} {int(b)} |  {int(c)}    | {  int(d)}    |   {int(c_or)}   |               {int(s)}     || {int(c)}"  )

        return and_inst, or_inst, not_inst,half_adder_inst, stimulus

    # Generate VCD File for waveform analysis
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()
    print("VCD file generated as 'gates.vcd'.")

# Run simulation
def test():
    simulate_gates()

test()
