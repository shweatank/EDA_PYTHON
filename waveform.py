import numpy as np
import matplotlib.pyplot as plt
import logging

# Configure logger to write logs to "waveform.log"
logging.basicConfig(
    filename="waveform.log",  # Log file
    level=logging.INFO,  # Log level
    format="%(asctime)s - %(levelname)s - %(message)s"  # Log format
)

logging.info("Starting waveform generation script.")

# Define the correct input sequences
A = np.array([0, 0, 1, 1])
B = np.array([0, 1, 0, 1])

logging.info(f"Input A: {A.tolist()}")
logging.info(f"Input B: {B.tolist()}")

# Repeat each state to maintain visualization clarity
t = np.linspace(0, 4, 400)
A_wave = np.repeat(A, 100)
B_wave = np.repeat(B, 100)

logging.info("Generated repeated waveforms for A and B.")

# Compute logic gate outputs
AND_output = A_wave & B_wave
OR_output = A_wave | B_wave
NOT_A = 1 - A_wave
NOT_B = 1 - B_wave
XOR_output = A_wave ^ B_wave
XNOR_output = 1 - XOR_output
NAND_output = 1 - AND_output
NOR_output = 1 - OR_output

logging.info("Computed logic gate outputs.")

# Plot waveforms
plt.figure(figsize=(10, 12))

def plot_waveform(position, signal, color, title):
    """Plots a logic gate waveform."""
    logging.info(f"Plotting {title} waveform.")
    plt.subplot(5, 2, position)
    plt.plot(t, signal, drawstyle="steps-pre", color=color, label=title)
    plt.ylim(-0.2, 1.2)
    plt.xticks([0.5, 1.5, 2.5, 3.5], ["00", "01", "10", "11"])
    plt.legend()


plot_waveform(1, A_wave, 'b', "Input A")
plot_waveform(2, B_wave, 'g', "Input B")
plot_waveform(3, AND_output, 'r', "AND Output")
plot_waveform(4, OR_output, 'm', "OR Output")
plot_waveform(5, NOT_A, 'c', "NOT A")
plot_waveform(6, NOT_B, 'y', "NOT B")
plot_waveform(7, XOR_output, 'brown', "XOR Output")
plot_waveform(8, XNOR_output, 'pink', "XNOR Output")
plot_waveform(9, NAND_output, 'purple', "NAND Output")
plot_waveform(10, NOR_output, 'darkblue', "NOR Output")

logging.info("All waveforms plotted successfully.")

plt.xlabel("Input States (A, B)")
plt.tight_layout()
plt.show()

logging.info("Waveform visualization displayed successfully.")