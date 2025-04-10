# from flask import Flask,render_template,jsonify
# import subprocess

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route('/and')
# def test_and():
#     subprocess.run(['make', 'GATE=and_gate', 'SIM_BUILD=results/and_gate'])
#     subprocess.run(["sudo",'gtkwave', 'and_gate.vcd'])
#     return jsonify({"message": "AND gate simulation completed."})

# @app.route('/or')
# def test_or():
#     subprocess.run(['make', 'GATE=or_gate'])
#     subprocess.run(["sudo",'gtkwave', 'or_gate.vcd'])
#     return jsonify({"message": "OR gate simulation completed."})

# @app.route('/not')
# def test_not():
#     subprocess.run(['make', 'GATE=not_gate'])
#     subprocess.run(["sudo",'gtkwave', 'not_gate.vcd'])
#     return jsonify({"message": "NOT gate simulation completed."})

# if __name__ == '__main__':
#     app.run()



from flask import Flask, render_template, jsonify, request
import subprocess
import os
from datetime import datetime
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB setup
client = MongoClient("mongodb://localhost:27017/")
db = client["gate_tests_db"]
collection = db["test_results"]

def store_test_result(gate_type, result, vcd_file):
    test_data = {
        "gate_type": gate_type,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "result": result,
        "vcd_file": vcd_file if os.path.exists(vcd_file) else None
    }
    collection.insert_one(test_data)

def get_test_history():
    return list(collection.find().sort("timestamp", -1).limit(10))

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/run_test', methods=['POST'])
def run_test():
    data = request.json
    gate_type = data['gate']
    
    try:
        # Run the test
        result = subprocess.run(
            ['make', f'GATE={gate_type}_gate', f'SIM_BUILD=results/{gate_type}_gate'],
            capture_output=True,
            text=True
        )
        
        output = result.stdout
        # More robust test result detection
        if "TESTS=1 PASS=1 FAIL=0" in output :
            test_status = "PASSED"
        else:
            test_status = "FAILED"
        
        vcd_file = f"{gate_type}_gate.vcd"
        
        # Store results with proper status
        store_test_result(gate_type, test_status, vcd_file)
        
        return jsonify({
            "status": "success",
            "gate": gate_type,
            "result": test_status,
            "output": output,
            "vcd_available": os.path.exists(vcd_file),
            "console_output": output  # For debugging
        })
        
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/view_waveform', methods=['POST'])
def view_waveform():
    try:
        data = request.json
        vcd_file = f"{data['gate']}_gate.vcd"
        
        if not os.path.exists(vcd_file):
            return jsonify({"status": "error", "message": "VCD file not found"}), 404
            
        # Run as regular user (remove sudo)
        #subprocess.Popen(["gtkwave", vcd_file])
        os.system('sudo gtkwave ' + vcd_file)

        
        return jsonify({"status": "success", "message": "GTKWave opened"})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
    
    
@app.route('/get_history', methods=['GET'])
def get_history():
    try:
        history = get_test_history()
        # Convert ObjectId to string for JSON serialization
        for item in history:
            item['_id'] = str(item['_id'])
        return jsonify({"status": "success", "history": history})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    os.makedirs("results", exist_ok=True)
    app.run(debug=True)