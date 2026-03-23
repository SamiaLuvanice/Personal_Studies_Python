from flask import Flask, redirect, render_template, request, url_for
from lista_filmes import buscar_filmes
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.sqlite3'

db = SQLAlchemy()
db.init_app(app)

conteudos = []
registros = []

@app.route('/', methods=['GET', 'POST'])
def principal():
    if request.method == 'POST':
        if request.form.get('conteudo'):
            conteudos.append(request.form.get('conteudo'))
            return redirect(url_for('principal'))

    return render_template(
        'index.html',
        conteudos=conteudos
    )

@app.route('/diario', methods=['GET', 'POST'])
def diario():
    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('nota'):
            aluno = request.form.get('aluno')
            nota = request.form.get('nota')
            registros.append(
                {
                    "aluno": aluno,
                    "nota": nota
                }
            )
            return redirect(url_for('diario'))

    return render_template(
        'sobre.html',
        registros=registros
    )

@app.route('/filmes/<propriedade>')
def lista_filmes(propriedade):
    return render_template(
        'filmes.html', 
        filmes=buscar_filmes(tipo=propriedade)
    )
