from myhdl import *
import pytest
#from half_adder import *

from half_adder import half_adder


@pytest.mark.parametrize("a_val, b_val, expected_s, expected_c", [
    (0, 0, 0, 0),
    (0, 1, 1, 0),
    (1, 0, 1, 0),
    (1, 1, 0, 1),
])
def test_half_adder(a_val, b_val, expected_s, expected_c):
    """Test half adder for all input combinations."""

    a, b, s, c = [Signal(bool(0)) for _ in range(4)]
    dut = half_adder(a, b, s, c)

    @instance
    def stimulus():
        a.next = a_val
        b.next = b_val
        yield delay(10)  # Allow time for propagation

        assert int(s) == expected_s, f"Sum mismatch: {int(s)} != {expected_s}"
        assert int(c) == expected_c, f"Carry mismatch: {int(c)} != {expected_c}"

    sim = Simulation(dut, stimulus)
    sim.run()

