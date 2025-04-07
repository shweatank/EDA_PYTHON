from flask import Flask, render_template
from flask_mysqldb import MySQL

app=Flask(__name__)
mysql=MySQL(app)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/or_gate')
def or_gate():
    return render_template('home.html')

@app.route('/and_gate')
def and_gate():
    return render_template('home.html')

@app.route('/not_gate')
def not_gate():
    return render_template('home.html')

app.run()