import matplotlib.pyplot as plt

# Input matrix
mat = [[0,0],[0,1],[1,0],[1,1]]
num = 0

def comp(num):
    return 1 if num == 0 else 0


and_outputs = [a & b for a, b in mat]
or_outputs = [a | b for a, b in mat]
not_output = [comp(num)]

# Time for visualization
time = range(len(mat))
time_not = [0, 1]

# Plot waveforms
plt.figure(figsize=(10, 6))

# Plot AND Operation
plt.subplot(3, 1, 1)
plt.step(time, and_outputs, where='post', label='AND', color='blue')
plt.ylim(-0.2, 1.2)
plt.yticks([0, 1])
plt.xticks([0,1,2,3,4])
plt.grid(True)
plt.legend()

# Plot OR Operation
plt.subplot(3, 1, 2)
plt.step(time, or_outputs, where='post', label='OR', color='green')
plt.ylim(-0.2, 1.2)
plt.yticks([0, 1])
plt.xticks([0,1,2,3,4])
plt.grid(True)
plt.legend()

# Plot NOT Operation
plt.subplot(3, 1, 3)
plt.step(time_not, not_output*2, where='post', label='NOT', color='red')
plt.ylim(-0.2, 1.2)
plt.yticks([0, 1])
plt.xticks([0,1,2,3,4])
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()