from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/fr")
def indexfr():
    return render_template("indexFr.html")

@app.route("/gpt")
def indexgpt():
    return render_template("indexgpt.html")