from flask import Flask
from myhdl import *
app=Flask(__name__)

def half_adder(a,b,s,c):
    @always_comb
    def logic():
        s.next=a ^ b
        c.next=a & b
    return logic

def AND_Gate(a,b,c):
    @always_comb
    def logic():
        c.next=a & b
    return logic

def OR_Gate(a,b,c):
    @always_comb
    def logic():
        c.next=a | b
    return logic


def NOT_Gate(a,b):
    @always_comb
    def logic():
        b.next=int(not a)
    return logic

app.route('/not_gate')
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
    return "VCD file generated as 'not_bench.vcd'."

@app.route('/or_gate')
def simulate_or_logic():
    a,b,c=[Signal(bool(0)) for _ in range(3)]

    def or_bench():
        or_inst=OR_Gate(a,b,c)

        @instance
        def stimulus():
            print('a b | c')
            print('----------------------')
            for i in range(2):
                for j in range(2):
                    a.next, b.next=i, j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(c)}')
    
        return or_inst, stimulus
    
    tb= traceSignals(or_bench)
    sim=Simulation(tb)
    sim.run()
    return "VCD file generated as 'or_bench.vcd'."


@app.route('/and_gate')
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
    return "VCD file generated as 'and_bench.vcd'."

@app.route('/halfadder')
def simulate_halfadder_logic():
    a,b,s,c=[Signal(bool(0)) for _ in range(4)]

    def halfadder_bench():
        halfadder_inst=half_adder(a,b,s,c)

        @instance
        def stimulus():
            print('a b | s c')
            print('----------------------')
            for i in range(2):
                for j in range(2):
                    a.next, b.next=i, j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(s)} {int(c)}')
    
        return halfadder_inst, stimulus
    
    tb= traceSignals(halfadder_bench)
    sim=Simulation(tb)
    sim.run()
    return "VCD file generated as 'halfadder_bench.vcd'."


if __name__=='__main__':
    app.run()