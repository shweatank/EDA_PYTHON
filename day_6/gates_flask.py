from myhdl import *
from flask import Flask, render_template, jsonify
from db import init_db,store
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/half_adder/<int:a>/<int:b>")
def half_adder(a, b):
    if a not in [0, 1] or b not in [0, 1]:
        return jsonify({"error": "Invalid inputs. Use 0 or 1."})

    sum_res = a ^ b
    carry_res = a & b
    return jsonify({"sum": sum_res, "carry": carry_res})


def AND_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = a & b
    return logic


@app.route("/and_gate")
def simulate_and_logic():
    a, b, c = [Signal(bool(0)) for _ in range(3)]

    def and_bench():
        and_inst = AND_Gate(a, b, c)

        @instance
        def stimulus():
            results = []
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)
                    results.append({"a": int(a), "b": int(b), "c": int(c)})
            return results

        return and_inst, stimulus

    tb = traceSignals(and_bench)
    sim = Simulation(tb)
    sim.run()
    store("and_bench.vcd")
    subprocess.run(["sudo", "gtkwave", "and_bench.vcd"])
    return jsonify({"message": "AND gate simulation completed."})


def OR_Gate(a, b, c):
    @always_comb
    def logic():
        c.next = a | b
    return logic


@app.route("/or_gate")
def simulate_or_logic():
    a, b, c = [Signal(bool(0)) for _ in range(3)]

    def or_bench():
        or_inst = OR_Gate(a, b, c)

        @instance
        def stimulus():
            results = []
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)
                    results.append({"a": int(a), "b": int(b), "c": int(c)})
            return results

        return or_inst, stimulus

    tb = traceSignals(or_bench)
    sim = Simulation(tb)
    sim.run()
    store("or_bench.vcd")
    subprocess.run(["sudo", "gtkwave", "or_bench.vcd"])
    return jsonify({"message": "OR gate simulation completed."})


def NOT_Gate(a, b):
    @always_comb
    def logic():
        b.next = int(not a)
    return logic


@app.route("/not_gate")
def simulate_not_logic():
    a, b = [Signal(bool(0)) for _ in range(2)]

    def not_bench():
        not_inst = NOT_Gate(a, b)

        @instance
        def stimulus():
            results = []
            for i in range(2):
                a.next = i
                yield delay(10)
                results.append({"a": int(a), "b": int(b)})
            return results

        return not_inst, stimulus

    tb = traceSignals(not_bench)
    sim = Simulation(tb)
    sim.run()
    store("not_bench.vcd")
    subprocess.run(["sudo", "gtkwave", "and_bench.vcd"])
    return jsonify({"message": "NOT gate simulation completed."})


if __name__ == "__main__":
    init_db()
    app.run(debug=True)