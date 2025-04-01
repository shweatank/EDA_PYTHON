from flask import Flask

app=Flask(__name__)

@app.route('/print')
def print():
    return "Hello World"

if __name__=='__main__':
    app.run(port=5000,debug=True)
