from flask import Flask, render_template, jsonify
import subprocess
import datetime
import os
import sqlite3

app = Flask(__name__)
log_file = "log.txt"
db_file = "logs.db"


# Initialize DB
def init_db():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            action TEXT,
            output TEXT
        )
    ''')
    conn.commit()
    conn.close()


def log(message, action="general"):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    # Log to file
    with open(log_file, "a") as f:
        f.write(f"{timestamp} {action.upper()}: {message}\n")
    # Log to DB
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("INSERT INTO logs (timestamp, action, output) VALUES (?, ?, ?)",
              (timestamp, action, message))
    conn.commit()
    conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/run_test', methods=['POST'])
def run_test():
    try:
        result = subprocess.run(['make'], capture_output=True, text=True)
        output = result.stdout + result.stderr
        log(output, "run_test")
        return jsonify({'status': 'success', 'output': output})
    except Exception as e:
        log(str(e), "run_test_error")
        return jsonify({'status': 'error', 'output': str(e)}), 500


@app.route('/run_synthesis', methods=['POST'])
def run_synthesis():
    try:
        # Step 1: Run Yosys synthesis and generate dot file
        yosys_script = """
        read_verilog spi_master.v
        hierarchy -check -top spi_master
        proc
        show -format dot -prefix spi_master_synth
        """
        with open("synth.ys", "w") as f:
            f.write(yosys_script)

        result = subprocess.run(['yosys', 'synth.ys'], capture_output=True, text=True)
        output = result.stdout + result.stderr
        log(output, "run_synthesis")

        # Step 2: Launch xdot or any other dot viewer (non-blocking)
        dot_file = "spi_master_synth.dot"
        if os.path.exists(dot_file):
            subprocess.Popen(['xdot', dot_file])  # Or use 'dot -Tpng ...' to render image
            log("Dot viewer launched for synthesis graph", "run_synthesis")
        else:
            output += "\n[WARN] Dot file not generated."

        return jsonify({'status': 'success', 'output': output})
    except Exception as e:
        log(f"Error in synthesis: {str(e)}", "run_synthesis_error")
        return jsonify({'status': 'error', 'output': str(e)}), 500


@app.route('/view_waveform', methods=['POST'])
def view_waveform():
    try:
        subprocess.Popen(['gtkwave', 'spi_master.vcd'])
        log("GTKWave launched", "view_waveform")
        return jsonify({'status': 'success', 'output': 'GTKWave launched'})
    except Exception as e:
        log(str(e), "view_waveform_error")
        return jsonify({'status': 'error', 'output': str(e)}), 500

@app.route('/verify_ml', methods=['POST'])
def verify_with_ml():
    try:
        # Run Makefile inside the "ml" folder
        result = subprocess.run(['make', '-C', 'ml'], capture_output=True, text=True)
        output = result.stdout + result.stderr
        log(output, "verify_with_ml")
        return jsonify({'status': 'success', 'output': output})
    except Exception as e:
        log(str(e), "verify_with_ml_error")
        return jsonify({'status': 'error', 'output': str(e)}), 500


@app.route('/netlist_validation', methods=['POST'])
def netlist_validation():
    try:
        # Run test_netlist.py
        result = subprocess.run(['python3', 'test_netlist.py'], capture_output=True, text=True)
        output = result.stdout + result.stderr
        log(output, "netlist_validation")
        return jsonify({'status': 'success', 'output': output})
    except Exception as e:
        log(str(e), "netlist_validation_error")
        return jsonify({'status': 'error', 'output': str(e)}), 500


@app.route('/log_output')
def log_output():
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = f.read()
        return render_template('logs.html', logs=logs)
    else:
        return "Log file not found", 404


@app.route('/db_logs')
def db_logs():
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    c.execute("SELECT timestamp, action, output FROM logs ORDER BY id DESC")
    rows = c.fetchall()
    conn.close()
    return render_template('db_logs.html', logs=rows)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)