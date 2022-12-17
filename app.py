from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>A simple test of a flask app!</h1><br>Leonardo Tavares'
