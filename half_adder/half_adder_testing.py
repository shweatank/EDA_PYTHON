import pytest


def and_gate(a: int, b: int) -> int:
    return a and b


def xor_gate(a: int, b: int) -> int:
    return a ^ b


def half_adder(a: int, b: int) -> tuple[int, int]:
    carry = and_gate(a, b)
    sum_result = xor_gate(a, b)
    return sum_result, carry


def run_demo():
    print("Half Adder Demo:")
    for a, b in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        sum_result, carry = half_adder(a, b)
        print(f"{a}, {b} => Sum: {sum_result}, Carry: {carry}")


def test_and_gate():
    assert and_gate(0, 0) == 0
    assert and_gate(0, 1) == 0
    assert and_gate(1, 0) == 0
    assert and_gate(1, 1) == 1


def test_xor_gate():
    assert xor_gate(0, 0) == 0
    assert xor_gate(0, 1) == 1
    assert xor_gate(1, 0) == 1
    assert xor_gate(1, 1) == 0


def test_half_adder():
    assert half_adder(0, 0) == (0, 0)
    assert half_adder(0, 1) == (1, 0)
    assert half_adder(1, 0) == (1, 0)
    assert half_adder(1, 1) == (0, 1)


if __name__ == "__main__":
    run_demo()

    # print("pytest file_path.py -v --cov=.")
