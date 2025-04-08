import csv
import random

# RAM configuration
D_WIDTH = 16
A_WIDTH = 5
DEPTH = 2 ** A_WIDTH

# Simulate memory
memory = [0] * DEPTH
truth_table = []

def write_ram(clock_cycle, address, data):
    memory[address] = data
    truth_table.append({
        "cycle": clock_cycle,
        "clk_write": "↑",
        "write_enable": 1,
        "address_write": address,
        "data_write": data,
        "clk_read": "-",
        "address_read": "-",
        "data_read": "-",
        "note": f"Write {data} to addr {address}"
    })

def read_ram(clock_cycle, address):
    data = memory[address]
    truth_table.append({
        "cycle": clock_cycle,
        "clk_write": "-",
        "write_enable": 0,
        "address_write": "-",
        "data_write": "-",
        "clk_read": "↑",
        "address_read": address,
        "data_read": data,
        "note": f"Read from addr {address}"
    })

def generate_truth_table():
    clock = 0
    # Step 1: Write random values
    for addr in range(DEPTH):
        data = random.randint(0, 2**D_WIDTH - 1)
        write_ram(clock, addr, data)
        clock += 1

    # Step 2: Read values back
    for addr in range(DEPTH):
        read_ram(clock, addr)
        clock += 1

    # Save to CSV
    with open("ram_truth_table.csv", "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=truth_table[0].keys())
        writer.writeheader()
        writer.writerows(truth_table)
    print("Truth table saved to ram_truth_table.csv")

if __name__ == "__main__":
    generate_truth_table()
