
from flask import Flask,render_template,jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route('/nand')
def test_nand():
    subprocess.run(['make', 'GATE=nand_gate'])
    subprocess.run(['gtkwave', 'dump.vcd'])
    return jsonify({"message": "NAND gate simulation completed."})

@app.route('/nor')
def test_nor():
    subprocess.run(['make', 'GATE=nor_gate'])
    subprocess.run(['gtkwave', 'dump.vcd'])
    return jsonify({"message": "NOR gate simulation completed."})

@app.route('/xor')
def test_xor():
    subprocess.run(['make', 'GATE=xor_gate'])
    subprocess.run(['gtkwave', 'dump.vcd'])
    return jsonify({"message": "XOR gate simulation completed."})

if __name__ == '__main__':
    app.run(port=5001)