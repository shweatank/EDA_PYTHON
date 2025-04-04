from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/and')
def test_and():
    subprocess.run(['make', 'GATE=and_gate', 'SIM_BUILD=results/and_gate'])
    subprocess.run(["sudo",'gtkwave', 'and_gate.vcd'])
    return "AND Gate Tested"

@app.route('/or')
def test_or():
    subprocess.run(['make', 'GATE=or_gate', 'SIM_BUILD=results/or_gate'])
    subprocess.run(["sudo",'gtkwave', 'or_gate.vcd'])
    return "OR Gate Tested"

@app.route('/not')
def test_not():
    subprocess.run(['make', 'GATE=not_gate', 'SIM_BUILD=results/not_gate'])
    subprocess.run(["sudo",'gtkwave', 'not_gate.vcd'])
    return "NOT Gate Tested"

if __name__ == '__main__':
    app.run()