import matplotlib.pyplot as plt
import numpy as np

# Input combinations for logic gates
inputs = [(0, 0), (0, 1), (1, 0), (1, 1)]


# Defining logic gate functions
def and_gate(a, b):
    return a and b


def or_gate(a, b):
    return a or b


def not_gate(a):
    return 1 if not a else 0


def nor_gate(a, b):
    return 1 if not (a or b) else 0


def nand_gate(a, b):
    return 1 if not (a and b) else 0


def xor_gate(a, b):
    return a ^ b


# Logic gate outputs
and_outputs = [and_gate(a, b) for a, b in inputs]
or_outputs = [or_gate(a, b) for a, b in inputs]
nor_outputs = [nor_gate(a, b) for a, b in inputs]
nand_outputs = [nand_gate(a, b) for a, b in inputs]
xor_outputs = [xor_gate(a, b) for a, b in inputs]

# NOT gate outputs (only for single input: 0,1)
not_inputs = [0, 1]
not_outputs = [not_gate(a) for a in not_inputs]

# Plot settings
fig, ax = plt.subplots(3, 2, figsize=(10, 10))
ax = ax.flatten()

# Plot each logic gate
ax[0].plot(and_outputs, "ro-", label="AND")
ax[0].set_title("AND Gate")

ax[1].plot(or_outputs, "bo-", label="OR")
ax[1].set_title("OR Gate")

ax[2].plot(nor_outputs, "go-", label="NOR")
ax[2].set_title("NOR Gate")

ax[3].plot(nand_outputs, "mo-", label="NAND")
ax[3].set_title("NAND Gate")

ax[4].plot(xor_outputs, "co-", label="XOR")
ax[4].set_title("XOR Gate")

ax[5].plot(not_inputs, not_outputs, "yo-", label="NOT")
ax[5].set_title("NOT Gate")

# Adjusting plots
for a in ax:
    a.set_xticks(range(len(inputs)))
    a.set_xticklabels([str(i) for i in inputs], rotation=45)
    a.set_yticks([0, 1])
    a.legend()
    a.grid(True)

plt.tight_layout()
plt.show()