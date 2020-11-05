from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect

app = Flask(__name__)

@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/saopaulo")
def saopaulo():
    return render_template("saopaulo.html")

@app.route("/corinthians")
def corinthians():
    return render_template("corinthians.html")

@app.route("/palmeiras")
def palmeiras():
    return render_template("palmeiras.html")

@app.route("/santos")
def santos():
    return render_template("santos.html")


app.run()