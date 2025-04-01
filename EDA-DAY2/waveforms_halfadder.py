import numpy as np
import matplotlib.pyplot as plt

# Define time intervals
t = np.linspace(0, 4, 400)  # Time axis

# Define the input waveforms A and B
A = np.repeat([0, 0, 1, 1], 100)  
B = np.repeat([0, 1, 0, 1], 100)  

# Compute half-adder outputs
Sum = A ^ B
Carry = A & B

# Function to plot waveforms
def plot_waveform(position, signal, color, title):
    plt.subplot(4, 1, position)  # 4 rows, 1 column
    plt.step(t, signal, where="post", color=color, linewidth=2, label=title)
    plt.ylim(-0.2, 1.2)
    plt.yticks([0, 1])
    plt.xticks([])
    plt.legend()

# Create figure
plt.figure(figsize=(8, 6))

plot_waveform(1, A, 'blue', "Input A")
plot_waveform(2, B, 'green', "Input B")
plot_waveform(3, Sum, 'red', "Sum (A XOR B)")
plot_waveform(4, Carry, 'purple', "Carry (A AND B)")

# Add labels
plt.xlabel("Time")
plt.tight_layout()
plt.show()
