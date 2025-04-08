from flask import Flask, render_template, request
from db import init_db, log_action
import subprocess
import os

app = Flask(__name__)
init_db()

# List of all gates/modules you want to test from your verilog/ and test_cases/
GATES = ['alu', 'and_gate', 'or_gate', 'not_gate', 'nand_gate', 'nor_gate', 'xor_gate', 'xnor_gate']

@app.route('/')
def index():
    return render_template('index.html', gates=GATES)

@app.route('/action', methods=['POST'])
def action():
    gate = request.form.get('operation')
    return render_template('action.html', operation=gate, result=None)

@app.route('/run_action', methods=['POST'])
def run_action():
    gate = request.form.get('operation')
    task = request.form.get('task')

    try:
        if task == 'test':
            result = subprocess.check_output(['make', f'GATE={gate}'], stderr=subprocess.STDOUT).decode()
        elif task == 'gtkwave':
            vcd_file = f"{gate}.vcd"
            if os.path.exists(vcd_file):
                subprocess.Popen(['gtkwave', vcd_file])
                result = f"📈 GTKWave launched for `{vcd_file}`."
            else:
                result = f"❌ `{vcd_file}` not found."
        elif task == 'synthesis':
            result = subprocess.check_output(['make', f'synth_{gate}'], stderr=subprocess.STDOUT).decode()
        elif task == 'netlist':
            try:
                result = subprocess.check_output(['make', f'netlist_test_{gate}'], stderr=subprocess.STDOUT).decode()
            except subprocess.CalledProcessError as e:
                result = f"❌ Netlist test failed:\n{e.output.decode()}"
        elif task == 'diagram':
            verilog_file = f"verilog/{gate}.v"
            yosys_script = f"""
            read_verilog {verilog_file}
            proc
            show -format svg -prefix static/diagram_{gate}
            """

            with open("diagram.ys", "w") as f:
                f.write(yosys_script)

            try:
                subprocess.check_output(['yosys', 'diagram.ys'], stderr=subprocess.STDOUT)
                result = f'<img src="/static/diagram_{gate}.svg" style="width:100%; border:1px solid #0ff; border-radius:10px;" />'
            except subprocess.CalledProcessError as e:
                result = f"❌ Yosys failed to generate diagram:\n<pre>{e.output.decode()}</pre>"
        else:
            result = "❌ Unknown task."

        log_action(gate, task, "Success", result)
        return render_template('action.html', operation=gate, result=result)

    except subprocess.CalledProcessError as e:
        error_output = e.output.decode()
        log_action(gate, task, "Fail", error_output)
        return render_template('action.html', operation=gate, result=error_output)

@app.route('/logs')
def show_logs():
    import sqlite3
    conn = sqlite3.connect("logs.db")
    c = conn.cursor()
    c.execute("SELECT * FROM logs ORDER BY id DESC")
    log_data = c.fetchall()
    conn.close()
    return render_template("logs.html", logs=log_data)

if __name__ == '__main__':
    app.run(debug=True)
