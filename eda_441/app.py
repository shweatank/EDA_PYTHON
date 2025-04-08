from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/action', methods=['POST'])
def action():
    operation = request.form.get('operation')
    return render_template('action.html', operation=operation)


def run_make_with_output(gate):
    try:
        result = subprocess.run(
            ['make', f'GATE={gate}', f'SIM_BUILD=results/{gate}'],
            capture_output=True,
            text=True,
            check=True
        )
        return True, result.stdout + result.stderr
    except subprocess.CalledProcessError as e:
        return False, e.stdout + e.stderr


@app.route('/run_action', methods=['POST', 'GET'])
def run_action():
    if request.method == 'GET':
        operation = request.args.get('operation')
        task = request.args.get('task')

        if task == 'test':
            success, output = run_make_with_output(operation)
            if success:
                return jsonify({"output": output})
            else:
                return jsonify({"output": output}), 500

        elif task == 'netlist':
            try:
                result = subprocess.run(
                    ["python3", "test_netlist_alu_json.py"],
                    cwd="Netlist_validation",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )
                output = result.stdout
                passed = output.count("... ok")
                failed = output.lower().count("fail")

                summary=''
                output += summary
                status = "✅ Netlist tests passed" if result.returncode == 0 else "❌ Netlist tests failed"
                return jsonify({"status": status, "output": output}), 200 if result.returncode == 0 else 500
            except Exception as e:
                return jsonify({"status": "❌ Error running netlist tests", "output": str(e)}), 500

        return jsonify({"output": "❌ Unsupported GET task."}), 400





    elif request.method == 'POST':
        operation = request.form.get('operation')
        task = request.form.get('task')

        if task == 'gtkwave':
            success, output = run_make_with_output(operation)
            if success:
                subprocess.run(['gtkwave', f'VCD/{operation}.vcd'], check=True)
                result = f"📈 GTKWave opened for {operation} (VCD waveform placeholder)"
        elif task == 'synthesis':
                # Run Yosys to generate the JSON netlist
            yosys_script = f"""
                    read_verilog verilog/{operation}.v
                    synth -top {operation}
                    write_json {operation}.json
                    """
            subprocess.run(["yosys", "-p", yosys_script], capture_output=True, text=True, check=True)
            import os
            json_path = os.path.join(os.getcwd(), f"{operation}.json")
            svg_path = os.path.join("static", f"{operation}.svg")
            # subprocess.run(['yosys','-p',f"read_verilog {operation}.v;",'proc;','show'])
            subprocess.run(["netlistsvg", json_path, "-o", svg_path], capture_output=True, text=True, check=True)
            return render_template("action.html", operation=operation,result=f'<img src="static/{operation}.svg" width="100%" />')

        elif task == 'netlist':
            try:
                result = subprocess.run(
                    ["python3", "test_netlist_alu_json.py"],
                    cwd="Netlist_validation",
                    stdout=subprocess.PIPE,
                    stderr=subprocess.STDOUT,
                    text=True
                )
                output = result.stdout
                passed = output.count("... ok")
                failed = output.lower().count("fail")

                summary = f"""
        ========================================
        ✅ Total Passed: {passed}
        ❌ Total Failed: {failed}
        ========================================
        """
                output += summary
                status = "✅ Netlist tests passed" if result.returncode == 0 else "❌ Netlist tests failed"
                return jsonify({"status": status, "output": output}), 200 if result.returncode == 0 else 500
            except Exception as e:
                return jsonify({"status": "❌ Error running netlist tests", "output": str(e)}), 500

        # elif task == 'netlist':
        #
        #     result = subprocess.run(
        #
        #         ["python3", "test_netlist_alu_json.py"],
        #
        #         cwd="Netlist_validation",
        #
        #         stdout=subprocess.PIPE,
        #
        #         stderr=subprocess.STDOUT,
        #
        #         text=True
        #
        #     )
        #
        #     success = result.returncode == 0
        #
        #     output = result.stdout
        #
        #     if success:
        #
        #         return jsonify({"status": "✅ Netlist tests passed", "output": output}), 200
        #
        #     else:
        #
        #         return jsonify({"status": "❌ Netlist tests failed", "output": output}), 500
        elif task == 'diagram':
            result = f"🧠 Diagram generated for {operation} (image path or render goes here)"
        else:
            result = "❌ Unknown task selected."
        return render_template('action.html', operation=operation, result=result)

    return jsonify({"message": "❌ Invalid request method or task."}), 400


if __name__ == '__main__':
    app.run(debug=True)
