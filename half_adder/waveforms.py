import matplotlib.pyplot as plt
import numpy as np
from half_adder import half_adder

t = np.array([0, 1, 2, 3, 4])
A = np.array([0, 0, 1, 1, 0])
B = np.array([0, 1, 0, 1, 0])
SUM, CARRY = half_adder(A, B)


fig, axs = plt.subplots(4, 1, figsize=(6, 6), sharex=True)

signals = [(A, "Input A"), (B, "Input B"), (SUM, "SUM"), (CARRY, "CARRY")]
colors = ['blue', 'red', 'green', 'purple']

for ax, (signal, title), color in zip(axs, signals, colors):
    ax.step(t, signal, where='post', linewidth=2)
    ax.set_ylim(-0.5, 1.5)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(["0", "1"])
    ax.set_title(title)
    ax.grid(False)

# Common X-axis settings
plt.xlabel("Time")
plt.xticks(t[:-1], labels=["T0", "T1", "T2", "T3"])

# Adjust layout and show plot
plt.tight_layout()
plt.show()
