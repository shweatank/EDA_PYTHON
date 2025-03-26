import pytest


def and_gate(a: int, b: int):
    return a and b


def or_gate(a: int, b: int):
    return a or b


def not_gate(a: int):
    return 1 if not a else 0


def nor_gate(a: int, b: int):
    return 1 if not (a or b) else 0


def nand_gate(a: int, b: int):
    return 1 if not (a and b) else 0


# AND
print("AND")
for i in range(2):
    for j in range(2):
        print(f"{i}, {j} = {and_gate(i, j)}")

# OR
print("OR")
for i in range(2):
    for j in range(2):
        print(f"{i}, {j} = {or_gate(i, j)}")

# NOT
print("NOT")
for i in range(2):
    print(f"{i} = {not_gate(i)}")


def test_and_gate():
    assert and_gate(0, 0) == 0
    assert and_gate(0, 1) == 0
    assert and_gate(1, 0) == 0
    assert and_gate(1, 1) == 1


def test_or_gate():
    assert or_gate(0, 0) == 0
    assert or_gate(0, 1) == 1
    assert or_gate(1, 0) == 1
    assert or_gate(1, 1) == 1


def test_not_gate():
    assert not_gate(0) == 1
    assert not_gate(1) == 0
