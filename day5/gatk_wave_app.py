from myhdl import *
from flask import Flask, jsonify
import sqlite3
import os
import time

app = Flask(__name__)

# Initialize SQLite Database
def init_db():
    conn = sqlite3.connect('simulation_logs.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY,
            a INTEGER,
            b INTEGER,
            and_result INTEGER,
            or_result INTEGER,
            not_result INTEGER,
            half_adder_sum INTEGER,
            half_adder_carry INTEGER,
            timestamp TEXT,
            vcd_filename TEXT  -- New column for storing VCD filename
        )
    ''')
    conn.commit()
    conn.close()

# AND Gate
def and_gate(a, b, c):
    """
    Basic AND gate: Implements a simple two-input AND gate.
    a, b -> Inputs
    c -> Output
    """
    @always_comb
    def logic():
        c.next = a & b
    return logic

# OR Gate
def or_gate(a, b, c):
    """
    Basic OR gate: Implements a simple two-input OR gate.
    a, b -> Inputs
    c -> Output
    """
    @always_comb
    def logic():
        c.next = a or b
    return logic

# NOT Gate (Inverter)
def not_gate(a, b):
    """
    Basic NOT gate: Implements a single-input NOT gate.
    a -> Input
    b -> Output
    """
    @always_comb
    def logic():
        b.next = not a
    return logic

# Half Adder
def half_adder(a, b, s, c):
    """
    Half Adder logic: Implements a simple half adder.
    a, b -> Inputs
    s -> Sum Output
    c -> Carry Output
    """
    @always_comb
    def logic():
        s.next = a ^ b
        c.next = a & b
    return logic

# Save Simulation Results and VCD Filename to SQLite Database
def save_to_db(a, b, c, d, c_or, s, c_half_adder, vcd_filename):
    conn = sqlite3.connect('simulation_logs.db')
    cursor = conn.cursor()
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO logs (a, b, and_result, or_result, not_result, half_adder_sum, half_adder_carry, timestamp, vcd_filename)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (a, b, c, d, c_or, s, c_half_adder, timestamp, vcd_filename))
    conn.commit()
    conn.close()

# Simulation for AND, OR, and NOT gates
@app.route('/simulate')
def simulate_gates():
    a, b, c, d = [Signal(bool(0)) for _ in range(4)]
    c_or, d_or = [Signal(bool(0)) for _ in range(2)]  # OR gate outputs
    s, c = [Signal(bool(0)) for _ in range(2)]

    # Generate the VCD filename
    vcd_filename = 'simulation_results_' + time.strftime('%Y%m%d_%H%M%S') + '.vcd'

    def bench():
        # Create instances for the logic gates
        and_inst = and_gate(a, b, c)
        or_inst = or_gate(a, b, d)
        not_inst = not_gate(a, c_or)
        half_adder_inst = half_adder(a, b, s, c)

        # Stimulus to drive the input signals and observe the outputs
        @instance
        def stimulus():
            output_data = []
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)  # Wait for a simulation time step
                    output_data.append({
                        'a': int(a),
                        'b': int(b),
                        'and': int(c),
                        'or': int(d),
                        'not': int(c_or),
                        'half_adder_sum': int(s),
                        'half_adder_carry': int(c)
                    })
                    # Save results to the database
                    save_to_db(int(a), int(b), int(c), int(d), int(c_or), int(s), int(c), vcd_filename)

            return jsonify(output_data)

        return and_inst, or_inst, not_inst, half_adder_inst, stimulus

    # Generate the simulation result
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()

    # Save VCD file
    with open(vcd_filename, 'w') as vcd:
        vcd.write("Generated VCD file\n")
    print(f"VCD file saved as {vcd_filename}")

    # Save VCD filename and results to the database
    save_to_db(int(a), int(b), int(c), int(d), int(c_or), int(s), int(c), vcd_filename)

    return f"Simulation completed successfully. VCD file saved as {vcd_filename}, and results stored in the database."

# Run the app
if __name__ == '__main__':
    init_db()  # Initialize the database when the app starts
    app.run(port=5000, debug=True)
