from myhdl import *
from flask import Flask, render_template, jsonify

import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/vcd_ram")
def ram():
    subprocess.run(["sudo", "gtkwave", "ram.vcd"])

@app.route("/rtl_verification")
def rtl_verification():
    subprocess.run(["make"])

if __name__ == "__main__":
    app.run(debug=True)
