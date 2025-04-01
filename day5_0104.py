from  flask import Flask, jsonify
from myhdl import *

# Define the AND gate logic
def and_gate(a, b, c):
    """
    Basic AND gate: Implements a simple two-input AND gate.
    a, b -> Inputs
    c -> Output
    """
    @always_comb
    def logic():
        c.next = a & b
    return logic

# Simulation function
def simulate_and_gate():
    a, b, c = [Signal(bool(0)) for _ in range(3)]

    def bench():
        and_inst = and_gate(a, b, c)

        @instance
        def stimulus():
            results = []
            for i in range(2):
                for j in range(2):
                    a.next, b.next = i, j
                    yield delay(10)
                    results.append((int(a), int(b), int(c)))
            return results

        return and_inst, stimulus

    # Generate VCD file for waveform analysis (optional)
    tb = traceSignals(bench)
    sim = Simulation(tb)
    sim.run()

    # Return simulation results as a list of tuples
    results = stimulus()
    return results

# Flask Application
app = Flask(__name__)

@app.route('/simulate', methods=['GET'])
def simulate():
    """
    Endpoint to run the AND gate simulation and return results.
    """
    results = simulate_and_gate()
    response = {
        "simulation_results": [
            {"a": res[0], "b": res[1], "c": res[2]} for res in results
        ]
    }
    return jsonify(response)

# Run Flask Application
if __name__ == '__main__':
    app.run(debug=True)
