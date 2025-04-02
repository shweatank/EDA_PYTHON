#--------------------------------------------------app.py----------------------------------------------
from flask import Flask, render_template, request
from myhdl import *
from flask_sqlalchemy import SQLAlchemy
import os

# Flask App Initialization
app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///simulation_logs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Model
class SimulationLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gate_type = db.Column(db.String(50))
    simulation_result = db.Column(db.String(200))
    vcd_file = db.Column(db.String(200))

# Create the database inside the application context
with app.app_context():
    db.create_all()

# Logic Gate Functions
def AND_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = a & b
    return logic

def NAND_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = not (a & b)
    return logic

def OR_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = a | b
    return logic

def NOR_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = not (a | b)
    return logic

def XOR_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = a ^ b
    return logic

def XNOR_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = not (a ^ b)
    return logic

def NOT_Gate(a, b):
    @always_comb
    def logic():
        b.next = int(not a)
    return logic

# Simulation Function with Logging & VCD Generation
def simulate_gate(gate_func, a_vals, b_vals=None):
    a, b, c = [Signal(bool(0)) for _ in range(3)]
    vcd_filename = f"{gate_func._name_}_simulation.vcd"

    # Simulation Bench
    def bench():
        gate_inst = gate_func(a, b, c) if b_vals else gate_func(a, b)
        @instance
        def stimulus():
            for i in a_vals:
                for j in b_vals if b_vals else [0]:
                    a.next, b.next = i, j
                    yield delay(10)
        return gate_inst, stimulus

    # Trace Signals to VCD File
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()

    # Log Simulation in Database
    log_entry = SimulationLog(
        gate_type=gate_func._name_,
        simulation_result="Success",
        vcd_file=vcd_filename
    )
    db.session.add(log_entry)
    db.session.commit()

    return f"Simulation complete for {gate_func._name.replace('', ' ').title()}. VCD saved as {vcd_filename}."

# Flask Routes
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/simulate/<gate>")
def simulate(gate):
    try:
        if gate == "and_gate":
            return simulate_gate(AND_Gate, [0, 1], [0, 1])
        elif gate == "nand_gate":
            return simulate_gate(NAND_Gate, [0, 1], [0, 1])
        elif gate == "or_gate":
            return simulate_gate(OR_Gate, [0, 1], [0, 1])
        elif gate == "nor_gate":
            return simulate_gate(NOR_Gate, [0, 1], [0, 1])
        elif gate == "xor_gate":
            return simulate_gate(XOR_Gate, [0, 1], [0, 1])
        elif gate == "xnor_gate":
            return simulate_gate(XNOR_Gate, [0, 1], [0, 1])
        elif gate == "not_gate":
            return simulate_gate(NOT_Gate, [0, 1])
        else:
            return "Invalid gate. Please choose a valid gate."
    except Exception as e:
        return f"An error occurred: {e}"

@app.route("/logs")
def view_logs():
    logs = SimulationLog.query.all()
    return render_template("logs.html", logs=logs)

if _name_ == "_main_":
    app.run(debug=True)
