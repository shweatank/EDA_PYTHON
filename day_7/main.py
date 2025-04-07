from flask import Flask,render_template,jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/and')
def test_and():
    subprocess.run(['make', 'GATE=and_gate', 'SIM_BUILD=results/and_gate'])
    subprocess.run(['gtkwave', 'and_gate.vcd'])
    return jsonify({"message": "AND gate simulation completed."})

@app.route('/or')
def test_or():
    subprocess.run(['make', 'GATE=or_gate'])
    subprocess.run(['gtkwave', 'or_gate.vcd'])
    return jsonify({"message": "OR gate simulation completed."})

@app.route('/not')
def test_not():
    subprocess.run(['make', 'GATE=not_gate'])
    subprocess.run(['gtkwave', 'not_gate.vcd'])
    return jsonify({"message": "NOT gate simulation completed."})

if __name__ == '__main__':
    app.run(port=5002)