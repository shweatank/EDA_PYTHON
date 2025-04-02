import os
from datetime import datetime
from flask import Flask
from myhdl import *
import sqlite3

app = Flask(__name__)

def create_table():
    # Connect to the SQLite database
    conn = sqlite3.connect('gates_simulation.db')
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS simulation_logs (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        gate_name TEXT NOT NULL,
        log_file TEXT NOT NULL,
        vcd_file TEXT NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')

    # Commit and close the connection
    conn.commit()
    conn.close()
create_table()

def half_adder(a,b,s,c):
    @always_comb
    def logic():
        s.next=a ^ b
        c.next=a & b
    return logic

def AND_Gate(a,b,c):
    @always_comb
    def logic():
        c.next=a & b
    return logic

def OR_Gate(a,b,c):
    @always_comb
    def logic():
        c.next=a | b
    return logic

def NOT_Gate(a,b):
    @always_comb
    def logic():
        b.next=int(not a)
    return logic

def insert_log(gate_name, log_file, vcd_file):
    # Connect to the SQLite database
    conn = sqlite3.connect('gates_simulation.db')
    cursor = conn.cursor()

    # Insert the log entry into the database
    cursor.execute('''
    INSERT INTO simulation_logs (gate_name, log_file, vcd_file)
    VALUES (?, ?, ?)
    ''', (gate_name, log_file, vcd_file))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

def simulate_gate_logic(gate_name, logic_function, vcd_filename):
    # Generate the VCD file
    result = logic_function()
    
    # Create log entry
    log_file = f"{gate_name}_log.txt"
    with open(log_file, 'w') as log:
        log.write(f"{datetime.now()}: {gate_name} simulation executed.\n")
    
    # Insert the log and VCD file details into the database
    insert_log(gate_name, log_file, vcd_filename)

    # Return the VCD file message
    return f"VCD file generated as '{vcd_filename}'."


@app.route('/not_gate')
def simulate_not_logic():
    a, b = [Signal(bool(0)) for _ in range(2)]

    def not_bench():
        not_inst = NOT_Gate(a, b)

        @instance
        def stimulus():
            print('a | b')
            print('----------------------')
            for i in range(2):
                a.next = i
                yield delay(10)
                print(f'{int(a)} | {int(b)}')
    
        return not_inst, stimulus
    
    tb = traceSignals(not_bench)
    sim = Simulation(tb)
    sim.run()

    return simulate_gate_logic("NOT Gate", not_bench, "not_bench.vcd")


@app.route('/or_gate')
def simulate_or_logic():
    a, b, c = [Signal(bool(0)) for _ in range(3)]

    def or_bench():
        or_inst = OR_Gate(a, b, c)

        @instance
        def stimulus():
            print('a b | c')
            print('----------------------')
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(c)}')
    
        return or_inst, stimulus
    
    tb = traceSignals(or_bench)
    sim = Simulation(tb)
    sim.run()

    return simulate_gate_logic("OR Gate", or_bench, "or_bench.vcd")


@app.route('/and_gate')
def simulate_and_logic():
    a, b, c = [Signal(bool(0)) for _ in range(3)]

    def and_bench():
        and_inst = AND_Gate(a, b, c)

        @instance
        def stimulus():
            print('a b | c')
            print('----------------------')
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(c)}')
    
        return and_inst, stimulus
    
    tb = traceSignals(and_bench)
    sim = Simulation(tb)
    sim.run()

    return simulate_gate_logic("AND Gate", and_bench, "and_bench.vcd")


@app.route('/halfadder')
def simulate_halfadder_logic():
    a, b, s, c = [Signal(bool(0)) for _ in range(4)]

    def halfadder_bench():
        halfadder_inst = half_adder(a, b, s, c)

        @instance
        def stimulus():
            print('a b | s c')
            print('----------------------')
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)
                    print(f'{int(a)} {int(b)} | {int(s)} {int(c)}')
    
        return halfadder_inst, stimulus
    
    tb = traceSignals(halfadder_bench)
    sim = Simulation(tb)
    sim.run()

    return simulate_gate_logic("Half Adder", halfadder_bench, "halfadder_bench.vcd")


if __name__ == '__main__':
    app.run(debug=True)
