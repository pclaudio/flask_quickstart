from flask import Flask, abort, render_template, url_for
from os import environ

app = Flask(__name__)
username = environ.get("USERNAME")
password = environ.get("PASSWORD")
db_host = environ.get("DB_HOST")
db_port = environ.get("DB_PORT")


@app.route('/')
def home():
    return f'''
        <h1>Seja bem vindo ao super sistema ASDF!!!</h1>
        <br />
        <h2>Seu usuário é { username } e senha { password }</h2>
        <br />
        <h3>Você está acessando o banco de dados { db_host } na porta { db_port } </h3>
        <br />
        <h3>{ url_for('static', filename='style.css') }</h3>
    '''

@app.route("/info")
def get_user_info():
    user = {"firstname": "Cláudio", "lastname": "Pereira", "age": 41}
    return user


@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    return render_template("hello.html", name=name)


@app.route('/login')
def login():
    abort(404)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404
