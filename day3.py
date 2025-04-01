#--------------------------and simulation----------------------------------
from myhdl import *
def and_gate(a,b,c):
    """
    Basic and gate:Implements a simple two-input and gate.
    a,b->Inputs
    c->Output
    """
    @always_comb
    def logic():
        c.next = a & b
    return logic

#simulation
def simulate_and_gate():
    a,b,c = [Signal(bool(0)) for _ in range(3)]

    def bench():
        and_inst = and_gate(a,b,c)

        @instance
        def stimulus():
            print("a b | c")
            print("---------")
            for i in range(2):
                for j in range(2):
                    a.next,b.next = i, j
                    yield delay(10)
                    print(f"{int(a)} {int(b)} | {int(c)}")

        return and_inst, stimulus

    #Generate VCD File for waveform analysis
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()
    print("VCD file generated as 'and_gate.vcd'.")

#Run simulation
def test():
    simulate_and_gate()
test()
#------------------------------nand------------------------------
from myhdl import *
def NAND_Gate(a,b,c):
    @always_comb
    def logic():
        c.next= not(a & b)
    return logic

#simulation
def simulate_nand_gate():
    a,b,c=[Signal(bool(0)) for _ in range(3)]
    def bench():
        nand_inst=NAND_Gate(a,b,c)
        @instance
        def stimulus():
            print("a b | c")
            print("-------")
            for i in range(2):
                for j in range(2):
                    a.next, b.next=i,j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(c)}')
        return nand_inst,stimulus
    #generate vcd
    tb=traceSignals(bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as nand_gate.vcd")
#run
def test():
    simulate_nand_gate()
test()

#------------------------------------------nor simulation--------------------------------

from myhdl import *
def Nor_Gate(a,b,c):
    @always_comb
    def logic():
        c.next= not(a | b)
    return logic
#simulation
def simulate_nor_gate():
    a,b,c=[Signal(bool(0)) for _ in range(3)]
    def bench():
        nor_inst=Nor_Gate(a,b,c)
        @instance
        def stimulus():
            print("a b | c")
            print("-------")
            for i in range(2):
                for j in range(2):
                    a.next, b.next=i,j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(c)}')
        return nor_inst,stimulus
    #generate vcd
    tb=traceSignals(bench)
    sim=Simulation(tb)
    sim.run()
    print("VCD file generated as nor_gate.vcd ")
#run
def test():
    simulate_nor_gate()
test()
#-------------------------------not------------------------------
from myhdl import *
def not_gate(a,c):
    """
    Basic and gate:Implements a simple two-input and gate.
    a,b->Inputs
    c->Output
    """
    @always_comb
    def logic():
        c.next = ~a & 1
    return logic

#simulation
def simulate_not_gate():
    a,c = [Signal(bool(0)) for _ in range(2)]

    def bench():
        and_inst = not_gate(a,c)

        @instance
        def stimulus():
            print("a | c")
            print("---------")
            for i in range(2):

                a.next = i
                yield delay(10)
                print(f"{int(a)}  | {int(c)}")

        return and_inst, stimulus

    #Generate VCD File for waveform analysis
    tb = traceSignals(bench)           # traceSignal() is a sdl method
    sim = Simulation(tb)     # it is used to create VCD file.
    sim.run()
    print("VCD file generated as 'not_gate.vcd'.")

#Run simulation
def test():
    simulate_not_gate()
test()

#---------------------------or------------------------------
from myhdl import *
def or_gate(a,b,c):
    """
    Basic and gate:Implements a simple two-input and gate.
    a,b->Inputs
    c->Output
    """
    @always_comb
    def logic():
        c.next = a | b
    return logic

#simulation
def simulate_or_gate():
    a,b,c = [Signal(bool(0)) for _ in range(3)]

    def bench():
        and_inst = or_gate(a,b,c)

        @instance
        def stimulus():
            print("a b | c")
            print("---------")
            for i in range(2):
                for j in range(2):
                    a.next,b.next = i, j
                    yield delay(10)
                    print(f"{int(a)} {int(b)} | {int(c)}")

        return and_inst, stimulus

    #Generate VCD File for waveform analysis
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()
    print("VCD file generated as 'or_gate.vcd'.")

#Run simulation
def test():
    simulate_or_gate()
test()


