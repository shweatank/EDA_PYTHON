import matplotlib.pyplot as plt
import numpy as np


def and_gate(a: int, b: int):
    return a and b


def xor_gate(a: int, b: int):
    return a ^ b


def half_adder(a, b):
    carry = and_gate(a, b)
    sum_ = xor_gate(a, b)
    return sum_, carry


inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]

half_adder_outputs = [half_adder(a, b) for a, b in inputs]
sum_outputs = [out[0] for out in half_adder_outputs]
carry_outputs = [out[1] for out in half_adder_outputs]


input_labels = ["(0,0)", "(0,1)", "(1,0)", "(1,1)"]


fig, ax = plt.subplots(2, 1, figsize=(6, 6))


ax[0].plot(input_labels, sum_outputs, "bo-", linewidth=2, markersize=8)
ax[0].set_title("Half Adder - Sum Output")
ax[0].set_ylim(-0.2, 1.2)
ax[0].set_yticks([0, 1])
ax[0].grid(True)


ax[1].plot(input_labels, carry_outputs, "ro-", linewidth=2, markersize=8)
ax[1].set_title("Half Adder - Carry Output")
ax[1].set_ylim(-0.2, 1.2)
ax[1].set_yticks([0, 1])
ax[1].grid(True)


for a in ax:
    a.set_xlabel("Inputs (A, B)")
    a.set_ylabel("Output")


plt.tight_layout()
plt.show()
