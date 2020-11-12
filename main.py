from flask import Flask
from flask import render_template 
from flask import request 
from flask import url_for 
from flask import redirect 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Senha5070*@localhost/torcedor'
db = SQLAlchemy(app) 

class torcedor(db.Model):
    _tablename_ = "cadastro"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    email = db.Column(db.String(50))
    time = db.Column(db.String(50))
    def _init_(self, nome, email, time):
        self.nome = nome
        self.email = email
        self.time = time

db.create_all()

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

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")

@app.route("/cadastrar",methods=['GET', 'POST'])
def cadastrar():
    if request.method =="POST":
        nome = (request.form.get("nome"))
        email = (request.form.get("email"))
        time = (request.form.get("time"))
        if nome:
            f = torcedor(nome)
            db.session.add(f)
            db.session.commit()
        if email:
            g = torcedor(email)
            db.session.add(g)
            db.session.commit()
        if time:
            h = torcedor(time)
            db.session.add(h)
            db.session.commit()
    return redirect(url_for("index"))

app.run()