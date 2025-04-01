from myhdl import *

def full_adder(a, b, cin, sum_, carry):
    @always_comb
    def logic():
        sum_.next = (a ^ b)^cin
        carry.next = (a and b) or (cin and (a^b))
    return logic

# Simulation
def simulate_full_adder():
    a, b, cin, sum_, carry = [Signal(bool(0)) for _ in range(5)]

    def bench():
        not_inst = full_adder(a, b, cin, sum_, carry)
        @instance
        def stimulus():
            print("a  b  cin    sum  carry")
            print("-----------------------")
            for i in range(2):
                a.next = i
                for j in range(2):
                    b.next = j
                    for k in range(2):
                        cin.next = k
                        yield delay(10)
                        print(f"{int(a)}   {int(b)}   {int(cin)}      {int(sum_)}   {int(carry)}")
        return not_inst, stimulus

    # Generate VCD file for waveform analysis
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()
    print("VCD file generated")

# Run simulation
def test():
    simulate_full_adder()

test()

