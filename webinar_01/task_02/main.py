# Nie restartuje przy zmianach:
# flask --app main run --host=0.0.0.0

# Restart przy zmianie
# flask --app main --debug run --host=0.0.0.0

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/hello/<name>', methods=["GET"])
def say_hello(name):
    return render_template('say_hello.html', name=name)