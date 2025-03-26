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


def xor_gate(a: int, b: int):
    return 1 if (a and not b) or (not a and b) else 0


def xnor_gate(a: int, b: int):
    return 1 if (a and b) or (not a or not b) else 0
