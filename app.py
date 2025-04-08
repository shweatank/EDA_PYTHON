from flask import Flask, render_template, request, jsonify, send_file
import os
import subprocess
import csv
from datetime import datetime
import sqlite3
import io

app = Flask(__name__)
GATE_DIR = os.getcwd()
LOG_FILE = "eda_simulation_log.txt"
DB_FILE = "eda_files.db"

def init_db():
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS files (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                gate TEXT,
                file_name TEXT,
                file_type TEXT,
                content BLOB
            )
        ''')
        conn.commit()

def log_event(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    with open(LOG_FILE, "a") as f:
        f.write(f"{timestamp} {message}\n")

def store_gate_files_in_db(gate):
    gate_path = os.path.join(GATE_DIR, gate)
    files_to_store = ["truth_table.csv", f"{gate}.vcd", f"{gate}.v", "Makefile", f"{gate}.xml"]

    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        for fname in files_to_store:
            fpath = os.path.join(gate_path, fname)
            if os.path.exists(fpath):
                with open(fpath, "rb") as f:
                    content = f.read()
                file_type = os.path.splitext(fname)[1].lstrip(".") or "Makefile"
                cursor.execute("INSERT INTO files (gate, file_name, file_type, content) VALUES (?, ?, ?, ?)",
                               (gate, fname, file_type, content))
        conn.commit()

@app.route("/")
def index():
    gates = [d for d in os.listdir(GATE_DIR) if os.path.isdir(os.path.join(GATE_DIR, d)) and not d.startswith('.')]
    return render_template("index.html", gates=gates)

@app.route("/run_test", methods=["POST"])
def run_test():
    gate = request.json["gate"]
    gate_path = os.path.join(GATE_DIR, gate)
    try:
        log_event(f"Running test for gate: {gate}")
        output = subprocess.check_output("make", cwd=gate_path, shell=True, stderr=subprocess.STDOUT).decode()
        status = "Passed" if "passed" in output.lower() else "Failed"
        log_event(f"Test Output for {gate}:\n{output}")
        log_event(f"Test Status: {status}")
        store_gate_files_in_db(gate)
        return jsonify({"output": output, "status": status})
    except subprocess.CalledProcessError as e:
        error = e.output.decode()
        log_event(f"Test Failed for {gate}. Error:\n{error}")
        return jsonify({"error": error, "status": "Failed"})

@app.route("/get_truth_table", methods=["POST"])
def get_truth_table():
    gate = request.json["gate"]
    csv_path = os.path.join(GATE_DIR, gate, "truth_table.csv")
    if not os.path.exists(csv_path):
        log_event(f"Truth table not found for gate: {gate}")
        return jsonify({"error": "Truth table not found."})

    table = []
    with open(csv_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            table.append(row)

    log_event(f"Truth table for {gate} loaded:\n{table}")
    return jsonify({"table": table})

@app.route("/run_synthesis", methods=["POST"])
def run_synthesis():
    gate = request.json["gate"]
    gate_path = os.path.join(GATE_DIR, gate)
    verilog_file = next((os.path.join(gate_path, file) for file in os.listdir(gate_path)
                         if file.endswith(".v") and not file.startswith("syth_")), None)

    if not verilog_file:
        log_event(f"Synthesis failed: Verilog file not found for {gate}")
        return jsonify({"error": "Verilog file not found."})

    yosys_command = f'yosys -p "read_verilog {verilog_file}; proc; show"'
    try:
        subprocess.Popen(yosys_command, shell=True)
        log_event(f"Synthesis started for {gate} using Yosys")
        return jsonify({"message": f"🔧 Yosys synthesis started for {gate}."})
    except Exception as e:
        log_event(f"Synthesis error for {gate}: {str(e)}")
        return jsonify({"error": str(e)})

@app.route("/run_waveform", methods=["POST"])
def run_waveform():
    gate = request.json["gate"]
    vcd_file = os.path.join(GATE_DIR, gate, f"{gate}.vcd")
    if not os.path.exists(vcd_file):
        log_event(f"Waveform view failed: VCD file not found for {gate}")
        return jsonify({"error": "VCD file not found."})

    try:
        subprocess.Popen(f"gtkwave {vcd_file}", shell=True)
        log_event(f"GTKWave opened for {gate}")
        return jsonify({"message": "📈 GTKWave launched successfully."})
    except Exception as e:
        log_event(f"Waveform error for {gate}: {str(e)}")
        return jsonify({"error": str(e)})

@app.route("/get_logs", methods=["GET"])
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify({"logs": "Log file is empty."})
    with open(LOG_FILE, "r") as f:
        return jsonify({"logs": f.read()})

@app.route("/list_files", methods=["POST"])
def list_files():
    gate = request.json["gate"]
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT id, file_name FROM files WHERE gate=?", (gate,))
        files = cursor.fetchall()
        return jsonify({"files": files})

@app.route("/view_file/<int:file_id>")
def view_file(file_id):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT file_name, content FROM files WHERE id=?", (file_id,))
        result = cursor.fetchone()
        if result:
            fname, content = result
            try:
                decoded = content.decode("utf-8")
            except UnicodeDecodeError:
                decoded = "⚠️ Cannot display binary file."
            return jsonify({"filename": fname, "content": decoded})
        return jsonify({"error": "File not found."}), 404

@app.route("/download_file/<int:file_id>")
def download_file(file_id):
    with sqlite3.connect(DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT file_name, content FROM files WHERE id=?", (file_id,))
        result = cursor.fetchone()
        if result:
            fname, content = result
            return send_file(
                io.BytesIO(content),
                download_name=fname,
                as_attachment=True
            )
        return "File not found", 404

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
