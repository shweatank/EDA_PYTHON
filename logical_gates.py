def print_truth_table():
    print("Truth Table for AND Gate:")
    print("A B | AND")
    print("------------")
    for a in [0, 1]:
        for b in [0, 1]:
            print(f"{a} {b} | {a & b}")

    print("\nTruth Table for OR Gate:")
    print("A B | OR")
    print("-----------")
    for a in [0, 1]:
        for b in [0, 1]:
            print(f"{a} {b} | {a | b}")

    print("\nTruth Table for NOT Gate:")
    print("A | NOT")
    print("-------")
    for a in [0, 1]:
        print(f"{a} | {1 - a}")

# Call the function to print truth tables
print_truth_table()

import pytest
def generate_truth_table():
    and_table = [(a, b, a & b) for a in [0, 1] for b in [0, 1]]
    or_table = [(a, b, a | b) for a in [0, 1] for b in [0, 1]]
    not_table = [(a, 1 - a) for a in [0, 1]]
    return and_table, or_table, not_table
# print(generate_truth_table())
# # Expected truth tables
expected_and = [(0, 0, 0), (0, 1, 0), (1, 0, 0), (1, 1, 1)]
expected_or = [(0, 0, 0), (0, 1, 1), (1, 0, 1), (1, 1, 1)]
expected_not = [(0, 1), (1, 0)]

@pytest.mark.parametrize("a, b, expected", expected_and)
def test_and_gate(a, b, expected):
    assert (a & b) == expected, f"Failed for {a} AND {b}"

@pytest.mark.parametrize("a, b, expected", expected_or)
def test_or_gate(a, b, expected):
    assert (a | b) == expected, f"Failed for {a} OR {b}"

@pytest.mark.parametrize("a, expected", expected_not)
def test_not_gate(a, expected):
    assert (1 - a) == expected, f"Failed for NOT {a}"

import matplotlib.pyplot as plt
import numpy as np

def generate_truth_table():
    and_table = [(a, b, a & b) for a in [0, 1] for b in [0, 1]]
    or_table = [(a, b, a | b) for a in [0, 1] for b in [0, 1]]
    not_table = [(a, 1 - a) for a in [0, 1]]
    return and_table, or_table, not_table

def plot_waveform(truth_table, title, labels):
    time_steps = np.arange(len(truth_table))
    inputs = np.array(truth_table)[:, :-1]
    output = np.array(truth_table)[:, -1]

    plt.figure(figsize=(8, 4))
    plt.title(title)
    for i, label in enumerate(labels[:-1]):
        plt.step(time_steps, inputs[:, i], label=label, where='mid')

    plt.step(time_steps, output, label=labels[-1], where='mid', linewidth=2, linestyle='dashed', color='red')
    plt.xlabel("Time Steps")
    plt.ylabel("Logic Level")
    plt.yticks([0, 1], ["LOW", "HIGH"])
    plt.legend()
    plt.grid(True)
    plt.show()

# Generate truth tables
and_table, or_table, not_table = generate_truth_table()

# Plot waveforms
plot_waveform(and_table, "AND Gate Waveform", ["Input A", "Input B", "Output (A AND B)"])
plot_waveform(or_table, "OR Gate Waveform", ["Input A", "Input B", "Output (A OR B)"])
plot_waveform(not_table, "NOT Gate Waveform", ["Input A", "Output (NOT A)"])