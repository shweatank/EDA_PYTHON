from myhdl import *


def Full_adder(a, b, cin, sum, cout):
    @always_comb
    def logic():
        sum.next = a ^ b ^ cin
        cout.next = (a & b) | (b & cin) | (a & cin)

    return logic


# Simulation
def simulate_full_adder():
    a, b, cin, sum, cout = [Signal(bool(0)) for _ in range(5)]

    def bench():
        fadder_inst = Full_adder(a, b, cin, sum, cout)

        @instance
        def stimulus():
            print("a b cin | sum cout")
            print("-----------------")
            for i in range(2):
                for j in range(2):
                    for k in range(2):
                        a.next, b.next, cin.next = i, j, k
                        yield delay(10)
                        print(f'{int(a)} {int(b)} {int(cin)} | {int(sum)} {int(cout)}')

        return fadder_inst, stimulus

    # Generate VCD file
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()
    print("VCD file generated as bench.vcd")


# Run test
def test():
    simulate_full_adder()


test()
