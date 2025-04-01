import matplotlib.pyplot as plt

# Define 3-bit input combinations (A, B) for 8 time steps
A = [0, 0, 0, 0, 1, 1, 1, 1]
B = [0, 0, 1, 1, 0, 0, 1, 1]

# Compute Logic Gate Outputs
AND_output = [a & b for a, b in zip(A, B)]
OR_output = [a | b for a, b in zip(A, B)]
NOT_A_output = [1 - a for a in A]  # NOT Gate on A
NOT_B_output = [1 - b for b in B]  # NOT Gate on B

# Define x-axis (time steps)
time_steps = list(range(len(A)))

# Plot Signals
plt.figure(figsize=(7, 8))  # Adjust figure size

plt.subplot(6, 1, 1)
plt.step(time_steps, A, label="A", color="blue", where='mid')
plt.ylim(-0.2, 1.2)
plt.xticks(time_steps)
plt.yticks([0, 1])
plt.legend()
plt.grid(True)

plt.subplot(6, 1, 2)
plt.step(time_steps, B, label="B", color="green", where='mid')
plt.ylim(-0.2, 1.2)
plt.xticks(time_steps)
plt.yticks([0, 1])
plt.legend()
plt.grid(True)

plt.subplot(6, 1, 3)
plt.step(time_steps, AND_output, label="A AND B", color="red", where='mid')
plt.ylim(-0.2, 1.2)
plt.xticks(time_steps)
plt.yticks([0, 1])
plt.legend()
plt.grid(True)

plt.subplot(6, 1, 4)
plt.step(time_steps, OR_output, label="A OR B", color="purple", where='mid')
plt.ylim(-0.2, 1.2)
plt.xticks(time_steps)
plt.yticks([0, 1])
plt.legend()
plt.grid(True)

plt.subplot(6, 1, 5)
plt.step(time_steps, NOT_A_output, label="~A", color="orange", where='mid')
plt.ylim(-0.2, 1.2)
plt.xticks(time_steps)
plt.yticks([0, 1])
plt.legend()
plt.grid(True)

plt.subplot(6, 1, 6)
plt.step(time_steps, NOT_B_output, label="~B", color="brown", where='mid')
plt.ylim(-0.2, 1.2)
plt.xticks(time_steps)
plt.yticks([0, 1])
plt.legend()
plt.grid(True)

plt.tight_layout()  # Adjusts spacing to avoid overlap
plt