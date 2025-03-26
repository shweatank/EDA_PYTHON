import time


def and_gate(a: int, b: int):
    return a and b


def xor_gate(a: int, b: int):
    return a ^ b


def half_adder(a, b):
    carry = and_gate(a, b)
    sum = xor_gate(a, b)
    return sum, carry


with open("half_adder_log.log", "a") as log_file:
    log_file.write("\n=== Half Adder Testing Log ===\n")
    log_file.write(f"Test Run at: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
    log_file.write("=" * 55 + "\n")

    for i in range(2):
        for j in range(2):
            obj = half_adder(i, j)
            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
            output = f"[{timestamp}] Input: {i}, {j} => Sum: {obj[0]}, Carry: {obj[1]}"
            print(f"{i}, {j} => Sum: {obj[0]}, Carry: {obj[1]}")
            log_file.write(output + "\n")

    log_file.write("=" * 55 + "\n")
