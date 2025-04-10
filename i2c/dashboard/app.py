import os
import subprocess
import sqlite3
from datetime import datetime
from flask import Flask, render_template, request, jsonify, send_from_directory

app = Flask(__name__)

# SQLite database file
DATABASE = "i2c_db.db"

# Initialize the database and create the log table if it doesn't exist
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS log_table (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            level TEXT,
            source TEXT,
            message TEXT
        )
    """)
    conn.commit()
    conn.close()

# Store log entry into the database
def store(timestamp, level, source, message):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO log_table (timestamp, level, source, message) VALUES (?, ?, ?, ?)",
        (timestamp, level, source, message)
    )
    conn.commit()
    conn.close()

# Wrapper for logging—auto-generates timestamp
def log_to_db(message, level="INFO", source="system"):
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    store(timestamp, level, source, message)


# Define all supported process types with paths, commands, and outputs
BASE_DIR = os.path.expanduser("~/Downloads/i2c_/i2c")

PATHS = {
    "rtl": {
        "dir": BASE_DIR,
        "cmd": "make",
        "output": "results.xml"
    },
    "netlist": {
        "dir": os.path.join(BASE_DIR, "i2c_master_sys"),
        "cmd": "make",
        "output": "results.xml"
    },
    "synthesis": {
        "dir": os.path.join(BASE_DIR, "i2c_master_sys"),
        "cmd": "yosys synth.ys",
        "output": "synthesis_output.txt"
    },
    "schematic": {
        "dir": os.path.join(BASE_DIR, "i2c_master_sys"),
        "cmd": "yosys -p 'read_verilog i2c.v; synth; show -format png -prefix schematic'",
        "output": "schematic.png"
    },
    "gtkwave": {
        "dir": BASE_DIR,
        "cmd": "sudo gtkwave i2c.vcd",
        "output": None
    }
}

# Main page
@app.route('/')
def index():
    return render_template('index.html')  

# Serve generated schematic image
@app.route('/schematic')
def serve_schematic():
    synth_dir = PATHS['schematic']['dir']
    return send_from_directory(synth_dir, 'schematic.png')

# Run the requested process type
@app.route('/run', methods=['GET'])
def run_process():
    process_type = request.args.get('type')
    config = PATHS.get(process_type)

    # Invalid process type check
    if not config:
        log_to_db(f"Invalid process type requested: {process_type}", level="WARNING", source="flask")
        return jsonify({"error": "Invalid process type"}), 400

    try:
        log_to_db(f"Starting process: {process_type}", level="INFO", source=process_type)

        # Clean up old output files
        if process_type in ["rtl", "netlist"]:
            subprocess.run(["rm", "-f", "results.xml"], cwd=config["dir"])
        elif process_type == "schematic":
            subprocess.run(["rm", "-f", "schematic.png"], cwd=config["dir"])

        # Start the process
        proc = subprocess.Popen(
            config["cmd"],
            cwd=config["dir"],
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True
        )

        # Stream logs to frontend while also logging to database
        def generate():
            for line in proc.stdout:
                line = line.strip()
                log_to_db(line, level="DEBUG", source=process_type)
                yield f"data: {line}\n\n"

            proc.wait()
            log_to_db(f"Completed process: {process_type}", level="INFO", source=process_type)

            # If result file exists, stream it to frontend
            if process_type in ["rtl", "netlist"]:
                result_file = os.path.join(config["dir"], config["output"])
                if os.path.exists(result_file):
                    with open(result_file) as f:
                        content = f.read()
                        yield f"data: === RESULTS ===\n\n"
                        yield f"data: {content}\n\n"
                        log_to_db("Results file sent to client", level="INFO", source=process_type)

            yield "data: PROCESS_COMPLETE\n\n"

        return app.response_class(generate(), mimetype='text/event-stream')

    except Exception as e:
        # Catch any runtime errors and log them
        error_message = f"Error in process {process_type}: {str(e)}"
        log_to_db(error_message, level="ERROR", source=process_type)
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    init_db()  
    app.run(debug=True, port=5001)
