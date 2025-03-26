import numpy as np
import matplotlib.pyplot as plt

# Define time points (discrete steps)
t = np.array([0, 1, 2, 3, 4])  # Time points

# Define Input A and Input B based on truth tables
A = np.array([0, 0, 1, 1, 0])  # First input (cyclic for clarity)
B = np.array([0, 1, 0, 1, 1])  # Second input (cyclic)

# Compute logic gate outputs
AND_output = A & B  # Logical AND operation
OR_output = A | B   # Logical OR operation
XOR_output = A ^ B  # Logical XOR operation
NAND_output = ~(A & B) & 1  # Logical NAND operation
NOR_output = ~(A | B) & 1   # Logical NOR operation
XNOR_output = ~(A ^ B) & 1  # Logical XNOR operation
NOT_A = ~A & 1  # NOT operation on A
NOT_B = ~B & 1  # NOT operation on B

# Create a figure with subplots
plt.figure(figsize=(8, 12))

# Plot Input A
plt.subplot(5, 2, 1)
plt.step(t, A, label="Input A", where="post", linewidth=2, color="blue")
plt.ylabel("A")
plt.yticks([0, 1])
plt.xticks([])
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Plot Input B
plt.subplot(5, 2, 2)
plt.step(t, B, label="Input B", where="post", linewidth=2, color="green")
plt.ylabel("B")
plt.yticks([0, 1])
plt.xticks([])
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Plot AND Gate Output
plt.subplot(5, 2, 3)
plt.step(t, AND_output, label="A AND B", where="post", linewidth=2, color="red")
plt.ylabel("AND")
plt.yticks([0, 1])
plt.xticks([])
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Plot OR Gate Output
plt.subplot(5, 2, 4)
plt.step(t, OR_output, label="A OR B", where="post", linewidth=2, color="orange")
plt.ylabel("OR")
plt.yticks([0, 1])
plt.xticks([])
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Plot XOR Gate Output
plt.subplot(5, 2, 5)
plt.step(t, XOR_output, label="A XOR B", where="post", linewidth=2, color="purple")
plt.ylabel("XOR")
plt.yticks([0, 1])
plt.xticks([])
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Plot NAND Gate Output
plt.subplot(5, 2, 6)
plt.step(t, NAND_output, label="A NAND B", where="post", linewidth=2, color="brown")
plt.ylabel("NAND")
plt.yticks([0, 1])
plt.xticks([])
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Plot NOR Gate Output
plt.subplot(5, 2, 7)
plt.step(t, NOR_output, label="A NOR B", where="post", linewidth=2, color="pink")
plt.ylabel("NOR")
plt.yticks([0, 1])
plt.xticks([])
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Plot XNOR Gate Output
plt.subplot(5, 2, 8)
plt.step(t, XNOR_output, label="A XNOR B", where="post", linewidth=2, color="gray")
plt.ylabel("XNOR")
plt.yticks([0, 1])
plt.xticks([])
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Plot NOT A Output
plt.subplot(5, 2, 9)
plt.step(t, NOT_A, label="NOT A", where="post", linewidth=2, color="cyan")
plt.ylabel("NOT A")
plt.yticks([0, 1])
plt.xticks([])
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Plot NOT B Output
plt.subplot(5, 2, 10)
plt.step(t, NOT_B, label="NOT B", where="post", linewidth=2, color="yellow")
plt.ylabel("NOT B")
plt.yticks([0, 1])
plt.xlabel("Time")
plt.grid(True, linestyle="--", alpha=0.7)
plt.legend()

# Adjust layout and show the plot
plt.tight_layout()
plt.show()
