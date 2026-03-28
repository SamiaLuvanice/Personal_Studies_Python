from projeto import app, db
from flask import redirect, render_template, request, url_for
from projeto.lista_filmes import buscar_filmes
from projeto.livro import Livro

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

@app.route('/livros')
def lista_livros():
    livros = Livro.query.all()
    return render_template(
        'livros.html',
        livros=livros
    )

@app.route('/add_livro', methods=['GET', 'POST'])
def adiciona_livro():
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        valor = request.form.get('valor')

        if nome and descricao and valor:
            novo_livro = Livro(nome=nome, descricao=descricao, valor=int(valor))
            db.session.add(novo_livro)
            db.session.commit()
            return redirect(url_for('lista_livros'))

    return render_template('novo_livro.html')

@app.route('/<int:id>/atualiza_livro', methods=['GET', 'POST'])
def atualiza_livro(id):
    livro_bd = Livro.query.get_or_404(id)
    if request.method == 'POST':
        nome = request.form.get('nome')
        descricao = request.form.get('descricao')
        valor = request.form.get('valor')

        if nome and descricao and valor:
            livro_bd.nome = nome
            livro_bd.descricao = descricao
            livro_bd.valor = int(valor)

        db.session.commit()
        return redirect(url_for('lista_livros'))

    return render_template('atualiza_livro.html', livro=livro_bd)

@app.route('/<int:id>/remove_livro', methods=['POST'])
def remove_livro(id):
    livro_bd = Livro.query.get_or_404(id)
    db.session.delete(livro_bd)
    db.session.commit()
    return redirect(url_for('lista_livros'))
