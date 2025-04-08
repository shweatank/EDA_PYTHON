import csv

# Define logic gates

def XNOR(a, b):
    return 1 if a == b else 0

# Define the truth table
header = ["A", "B", "XNOR"]
rows = [[a, b, XNOR(a, b)] for a in [0, 1] for b in [0, 1]]

# Write to CSV without any extra lines or comments
with open("truth_table.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

print("✅ Truth table CSV generated successfully: truth_table.csv")