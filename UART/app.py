from flask import Flask, render_template, send_file, request
import subprocess
import os
import datetime
import sqlite3
import json

app = Flask(__name__)
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
DB_PATH = os.path.join(BASE_DIR, "logs.db")

os.makedirs(RESULTS_DIR, exist_ok=True)

# Global state to preserve outputs
last_run_output = ""
last_synth_output = ""
last_validation_output = ""

# Initialize SQLite DB
def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                type TEXT,
                content TEXT,
                timestamp TEXT
            )
        ''')
        conn.commit()

init_db()

# Save logs to SQLite
def save_log(log_type, content):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO logs (type, content, timestamp) VALUES (?, ?, ?)",
                       (log_type, content, timestamp))
        conn.commit()

# Netlist JSON validation logic
def validate_netlist(filepath):
    try:
        with open(filepath, 'r') as file:
            netlist = json.load(file)
    except json.JSONDecodeError as e:
        return False, f"Invalid JSON format: {e}"
    except FileNotFoundError:
        return False, "Netlist file not found."

    if "modules" not in netlist or not isinstance(netlist["modules"], dict):
        return False, "Missing or invalid 'modules' section in netlist."

    for module_name, module_data in netlist["modules"].items():
        if "ports" not in module_data or "cells" not in module_data or "netnames" not in module_data:
            return False, f"Module '{module_name}' missing 'ports', 'cells', or 'netnames'."
        if not isinstance(module_data["ports"], dict):
            return False, f"Module '{module_name}' ports must be a dictionary."
        if not isinstance(module_data["cells"], dict):
            return False, f"Module '{module_name}' cells must be a dictionary."
        if not isinstance(module_data["netnames"], dict):
            return False, f"Module '{module_name}' netnames must be a dictionary."

    return True, "Netlist Validation Done."

@app.route('/')
def index():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, type, timestamp FROM logs ORDER BY id DESC")
        logs = cursor.fetchall()
    return render_template('index.html',
                           result=last_run_output,
                           synth_result=last_synth_output,
                           validation_result=last_validation_output,
                           vcd=os.path.exists(os.path.join(RESULTS_DIR, "wave.vcd")),
                           logs=logs)

@app.route('/run_test')
def run_test():
    global last_run_output
    try:
        result = subprocess.run(["make", "-C", BASE_DIR], capture_output=True, text=True)
        output = result.stdout + "\n" + result.stderr
        last_run_output = output
        save_log("run", output)
    except Exception as e:
        last_run_output = str(e)

    return index()

@app.route('/synthesize')
def synthesize():
    global last_synth_output
    try:
        result = subprocess.run(["yosys", "-p", "read_verilog uart_tx.v; proc; show"], capture_output=True, text=True)
        output = result.stdout + "\n" + result.stderr
        last_synth_output = output
        save_log("synth", output)
    except Exception as e:
        last_synth_output = str(e)

    return index()

@app.route('/validate_netlist')
def validate_netlist_route():
    global last_validation_output
    filepath = os.path.join(RESULTS_DIR, "netlist.json")
    is_valid, message = validate_netlist(filepath)
    last_validation_output = message
    save_log("validate", message)
    return index()

@app.route('/waveform')
def waveform():
    vcd_path = os.path.join(RESULTS_DIR, "wave.vcd")
    if os.path.exists(vcd_path):
        subprocess.Popen(["gtkwave", vcd_path])
        return "GTKWave launched!"
    else:
        return "VCD file not found."

@app.route('/log/<int:log_id>')
def view_log(log_id):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT type, content, timestamp FROM logs WHERE id = ?", (log_id,))
        row = cursor.fetchone()
        if row:
            log_type, content, timestamp = row
            return f"<h2>{log_type.upper()} Log - {timestamp}</h2><pre>{content}</pre>"
        else:
            return "Log not found."

if __name__ == '__main__':
    app.run(debug=True, port=5002)