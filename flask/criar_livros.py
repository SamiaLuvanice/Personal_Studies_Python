from projeto import app, db
from projeto.livro import Livro

with app.app_context():
    # Criar tabelas
    db.create_all()

    # Adicionar alguns livros de teste
    livros = [
        Livro("1984", "Distopia futurista", 45),
        Livro("O Senhor dos Anéis", "Fantasia épica", 120),
        Livro("Python para Iniciantes", "Programação", 65)
    ]

    for item_livro in livros:
        db.session.add(item_livro)

    db.session.commit()
    print("✅ Livros criados com sucesso!")
