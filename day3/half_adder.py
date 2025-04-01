def half_adder(x: int, y: int):

    if x not in [0, 1] or y not in [0, 1]:
        raise ValueError("Inputs must be 0 or 1")

    sum_ = x ^ y  # XOR operation
    carry = x & y  # AND operation

    return sum_, carry


a = [(0, 0), (0, 1), (1, 0), (1, 1)]
print("sum carry")
for i, j in a:
    k = half_adder(i, j)
    print(k)
