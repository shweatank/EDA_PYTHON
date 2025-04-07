# from flask import Flask, render_template, request, jsonify
# import subprocess
# import datetime
# import os
#
# app = Flask(__name__)
# LOG_FILE = "logs.txt"
# VCD_FILE = "/home/mirafra/PycharmProjects/RAMTest/ram/waveform.vcd"
# DESIGN_FILE = "/home/mirafra/PycharmProjects/RAMTest/ram/design.v"
#
# def append_log(message):
#     timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
#     with open(LOG_FILE, "a") as log_file:
#         log_file.write(f"{timestamp} {message}\n")
#
# @app.route("/")
# def index():
#     return render_template("index.html")
#
# @app.route("/run_test", methods=["POST"])
# def run_test():
#     append_log("🔁 Running RAM test with make -C ...")
#     try:
#         result = subprocess.run(
#             ["make", "-C", "/home/mirafra/PycharmProjects/RAMTest/ram"],
#             stdout=subprocess.PIPE,
#             stderr=subprocess.PIPE,
#             text=True
#         )
#
#         # Full output from simulation
#         output = result.stdout + "\n" + result.stderr
#         append_log("🧪 Test Output:\n" + output)
#
#         # Look for "TESTS=1 PASS=1" to confirm success
#         if "TESTS=1" in output and "FAIL=0" in output:
#             status = "✅ Passed"
#         else:
#             status = "❌ Failed"
#
#         return jsonify({"status": status, "output": output})
#     except Exception as e:
#         error_msg = str(e)
#         append_log("❌ Error in test: " + error_msg)
#         return jsonify({"status": "Failed", "error": error_msg})
#
# @app.route("/run_synthesis", methods=["POST"])
# def run_synthesis():
#     append_log("🔁 Running synthesis...")
#     try:
#         command = f'yosys -p "read_verilog {DESIGN_FILE}; proc; show"'
#         result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
#         output = result.stdout + "\n" + result.stderr
#         append_log("🔧 Synthesis Output:\n" + output)
#         return jsonify({"status": "Success", "output": output})
#     except Exception as e:
#         append_log("❌ Error in synthesis: " + str(e))
#         return jsonify({"status": "Failed", "error": str(e)})
#
# @app.route("/run_waveform", methods=["POST"])
# def run_waveform():
#     append_log("📈 Opening GTKWave...")
#     try:
#         if not os.path.exists(VCD_FILE):
#             msg = "VCD file not found!"
#             append_log(msg)
#             return jsonify({"status": "Failed", "error": msg})
#
#         subprocess.Popen(["gtkwave", VCD_FILE])
#         append_log("✅ GTKWave opened.")
#         return jsonify({"status": "Success", "message": "GTKWave opened."})
#     except Exception as e:
#         append_log("❌ Error opening GTKWave: " + str(e))
#         return jsonify({"status": "Failed", "error": str(e)})
#
# @app.route("/get_logs")
# def get_logs():
#     if not os.path.exists(LOG_FILE):
#         return jsonify({"logs": ""})
#     with open(LOG_FILE, "r") as log_file:
#         logs = log_file.read()
#     return jsonify({"logs": logs})
#
# if __name__ == "__main__":
#     app.run(debug=True,port=5001)



from flask import Flask, render_template, request, jsonify
import subprocess
import datetime
import os
import sqlite3

app = Flask(__name__)
LOG_FILE = "logs.txt"
DB_FILE = "dashboard.db"
VCD_FILE = "/home/mirafra/PycharmProjects/RAMTest/ram/waveform.vcd"
DESIGN_FILE = "/home/mirafra/PycharmProjects/RAMTest/ram/design.v"

# Initialize DB and create table if not exists
def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

init_db()

# Append logs to both txt file and database
def append_log(message):
    timestamp = datetime.datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    log_entry = f"{timestamp} {message}"
    # Write to file
    with open(LOG_FILE, "a") as log_file:
        log_file.write(log_entry + "\n")
    # Write to SQLite DB
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO logs (timestamp, message) VALUES (?, ?)", (timestamp, message))
    conn.commit()
    conn.close()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/run_test", methods=["POST"])
def run_test():
    append_log("🔁 Running RAM test with make -C ...")
    try:
        result = subprocess.run(
            ["make", "-C", "/home/mirafra/PycharmProjects/RAMTest/ram"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        output = result.stdout + "\n" + result.stderr
        append_log("🧪 Test Output:\n" + output)

        status = "✅ Passed" if "TESTS=1" in output and "FAIL=0" in output else "❌ Failed"
        return jsonify({"status": status, "output": output})
    except Exception as e:
        error_msg = str(e)
        append_log("❌ Error in test: " + error_msg)
        return jsonify({"status": "Failed", "error": error_msg})

@app.route("/run_synthesis", methods=["POST"])
def run_synthesis():
    append_log("🔁 Running synthesis...")
    try:
        command = f'yosys -p "read_verilog {DESIGN_FILE}; proc; show"'
        result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        output = result.stdout + "\n" + result.stderr
        append_log("🔧 Synthesis Output:\n" + output)
        return jsonify({"status": "Success", "output": output})
    except Exception as e:
        append_log("❌ Error in synthesis: " + str(e))
        return jsonify({"status": "Failed", "error": str(e)})

@app.route("/run_waveform", methods=["POST"])
def run_waveform():
    append_log("📈 Opening GTKWave...")
    try:
        if not os.path.exists(VCD_FILE):
            msg = "VCD file not found!"
            append_log(msg)
            return jsonify({"status": "Failed", "error": msg})

        subprocess.Popen(["gtkwave", VCD_FILE])
        append_log("✅ GTKWave opened.")
        return jsonify({"status": "Success", "message": "GTKWave opened."})
    except Exception as e:
        append_log("❌ Error opening GTKWave: " + str(e))
        return jsonify({"status": "Failed", "error": str(e)})

@app.route("/get_logs")
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify({"logs": ""})
    with open(LOG_FILE, "r") as log_file:
        logs = log_file.read()
    return jsonify({"logs": logs})

@app.route("/get_logs_db")
def get_logs_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT timestamp, message FROM logs ORDER BY id DESC")
    data = c.fetchall()
    conn.close()
    logs = "\n".join([f"{ts} {msg}" for ts, msg in data])
    return jsonify({"logs": logs})

if __name__ == "__main__":
    app.run(debug=True, port=5002)
