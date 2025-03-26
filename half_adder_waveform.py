import numpy as np
import matplotlib.pyplot as plt

# Define input sequences
A = np.array([0, 0, 1, 1])  # Input A
B = np.array([0, 1, 0, 1])  # Input B

# Repeat values for better visualization
t = np.linspace(0, 4, 400)  # Time axis
A_wave = np.repeat(A, 100)
B_wave = np.repeat(B, 100)

# Compute Half Adder outputs
SUM_output = A_wave ^ B_wave  # XOR (Sum)
CARRY_output = A_wave & B_wave  # AND (Carry)

# Plot waveforms
plt.figure(figsize=(8, 6))

def plot_waveform(position, signal, color, title):
    """Plots a logic gate waveform."""
    plt.subplot(3, 1, position)
    plt.plot(t, signal, drawstyle="steps-pre", color=color, linewidth=2, label=title)
    plt.ylim(-0.2, 1.2)
    plt.xticks([0.5, 1.5, 2.5, 3.5], ["00", "01", "10", "11"])
    plt.legend()

# Plot Input A, B, Sum, and Carry
plot_waveform(1, A_wave, 'b', "Input A")
plot_waveform(2, B_wave, 'g', "Input B")
plot_waveform(3, SUM_output, 'r', "SUM (A XOR B)")
plot_waveform(3, CARRY_output, 'purple', "CARRY (A AND B)")

plt.xlabel("Input States (A, B)")
plt.tight_layout()
plt.show()
