from flask import Flask
from flask import render_template 
from flask import request 
from flask import url_for 
from flask import redirect 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:admin@localhost/torcedor'
db = SQLAlchemy(app) 

class torcedor(db.Model):
    __tablename__ = "cadastro"
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50))
    sexo = db.Column(db.String(1))
    email = db.Column(db.String(50))
    telefone = db.Column(db.String(15))
    time = db.Column(db.String(50))
    newsletter = db.Column(db.String(5))
    def __init__(self, nome, sexo, email, telefone, time, newsletter):
        self.nome = nome
        self.sexo = sexo
        self.email = email
        self.telefone = telefone
        self.time = time
        self.newsletter = newsletter

db.create_all()

@app.route("/")
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

@app.route("/msg_cad_sucesso")
def msg_cad_sucesso():
    return render_template("msg_cad_sucesso.html")

@app.route("/cadastrar",methods=['GET', 'POST'])
def cadastrar():
    if request.method =="POST":
        nome = (request.form.get("nome"))
        sexo = (request.form.get("sexo"))
        email = (request.form.get("email"))
        telefone = (request.form.get("telefone"))
        time = (request.form.get("time"))
        newsletter = (request.form.get("newsletter"))
        if nome:
            f = torcedor(nome,sexo,email,telefone,time,newsletter)
            db.session.add(f)
            db.session.commit()
    return redirect(url_for("msg_cad_sucesso"))

@app.route("/listarsocios")
def listarsocios():
    torcedores = torcedor.query.all()
    return render_template("listar_socios.html", torcedores=torcedores)

app.run()