# app.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/about')
def about():
    return "This is a simple Flask app!"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    app.run(debug=True)
