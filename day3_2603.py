import matplotlib.pyplot as plt

# Input matrix for a half adder (A, B)
mat = [[0,0],[0,1],[1,0],[1,1]]
time = range(len(mat))

# Perform half adder operations
sum_outputs = [a ^ b for a, b in mat]
carry_outputs = [a & b for a, b in mat]
a_inputs = [a for a, b in mat]
b_inputs = [b for a, b in mat]

# Plot waveforms
plt.figure(figsize=(8, 14))

# Plot Input A
plt.subplot(4, 1, 1)
plt.step(time, a_inputs, where='post', label='Input A', color='purple')
plt.ylim(-0.2, 1.2)
plt.xlim(-0.5, len(mat) - 0.5)
plt.xticks(time)
plt.yticks([0, 1])
plt.grid(True)
plt.legend()

# Plot Input B
plt.subplot(4, 1, 2)
plt.step(time, b_inputs, where='post', label='Input B', color='orange')
plt.ylim(-0.2, 1.2)
plt.xlim(-0.5, len(mat) - 0.5)
plt.xticks(time)
plt.yticks([0, 1])
plt.grid(True)
plt.legend()

# Plot SUM (XOR)
plt.subplot(4, 1, 3)
plt.step(time, sum_outputs, where='post', label='SUM (A XOR B)', color='blue')
plt.ylim(-0.2, 1.2)
plt.xlim(-0.5, len(mat) - 0.5)
plt.xticks(time)
plt.yticks([0, 1])
plt.grid(True)
plt.legend()

# Plot CARRY (AND)
plt.subplot(4, 1, 4)
plt.step(time, carry_outputs, where='post', label='CARRY (A AND B)', color='green')
plt.ylim(-0.2, 1.2)
plt.xlim(-0.5, len(mat) - 0.5)
plt.xticks(time)
plt.yticks([0, 1])
plt.grid(True)
plt.legend()

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()
