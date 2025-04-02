from flask import Flask,render_template


app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def home():
    return render_template('gate_html.html')

app.run(port=5000,debug=True)