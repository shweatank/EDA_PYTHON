def full_adder(A: int, B: int, Cin: int):
    """
    Full Adder Function
    Inputs: A, B, Cin (0 or 1)
    Outputs: Sum, Cout (0 or 1)
    """
    if A not in [0, 1] or B not in [0, 1] or Cin not in [0, 1]:
        raise ValueError("Inputs must be 0 or 1")

    Sum = A ^ B ^ Cin
    Cout = (A & B) | (B & Cin) | (A & Cin)
    return Sum, Cout
