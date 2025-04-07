from flask import Flask, render_template, request, jsonify
import subprocess
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logs.db'
db = SQLAlchemy(app)

class Log(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    logger = db.Column(db.String)
    level = db.Column(db.String)
    message = db.Column(db.String)
    creation_date = db.Column(db.DateTime, nullable=False, server_default=func.now())

# Create the database tables within the application context
with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/logic', methods=['POST'])
def logic_gate():
    data = request.json
    gate_type = data.get('gate')
    input_a = data.get('input_a')
    input_b = data.get('input_b')

    if gate_type == 'AND':
        output = input_a and input_b
    elif gate_type == 'OR':
        output = input_a or input_b
    elif gate_type == 'NOT':
        output = not input_a
    elif gate_type == 'NAND':
        output = not (input_a and input_b)
    elif gate_type == 'NOR':
        output = not (input_a or input_b)
    elif gate_type == 'XOR':
        output = input_a != input_b
    else:
        return jsonify({'error': 'Invalid gate type'}), 400

    log_entry = Log(logger='LogicGate', level='INFO', message=f"{gate_type} gate with inputs {input_a}, {input_b} produced output {output}")
    db.session.add(log_entry)
    db.session.commit()

    return jsonify({'output': int(output)})

@app.route('/simulate/<gate_type>', methods=['GET'])
def simulate_gate(gate_type):
    try:
        subprocess.run(['make', f'GATE={gate_type}', 'SIM_BUILD=results/' + gate_type], check=True)
        subprocess.run(['gtkwave', f'{gate_type}.vcd'], check=True)
        return jsonify({"message": f"{gate_type.upper()} gate simulation completed."})
    except subprocess.CalledProcessError as e:
        return jsonify({"error": f"Simulation failed: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)