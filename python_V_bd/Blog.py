from conexao_orm import Base, engine, session
from User import User
from Post import Post

# Cria as tabelas no banco de dados
Base.metadata.create_all(engine)

# Exibir menu de opções
def show_menu():
    print("Menu de opções:")
    print("1. Adicionar usuário")
    print("2. Adicionar post")
    print("3. Listar usuários e seus posts")
    print("4. Sair")

# Adiciona um novo usuário
def add_user():
  print("Adicionar usuário")
  name = input("Digite o nome do usuário: ")
  email = input("Digite o email do usuário: ")
  user = User(name, email)
  session.add(user)
  session.commit()
  print("Usuário adicionado com sucesso!")

# Adiciona novo post
def add_post():
  print("Adicionar post")
  title = input("Digite o título do post: ")
  content = input("Digite o conteúdo do post: ")
  author_id = int(input("Digite o ID do autor do post: "))
  user = session.query(User).filter_by(id=author_id).first()
  if user:
    post = Post(title=title, content=content, author=user)
    session.add(post)
    session.commit()
    print("Post adicionado com sucesso!")
  else:
    print("Autor não encontrado. Por favor, adicione um usuário válido.")

# Consulta e exibe os usuários e seus posts
def query_user_posts():
  print("Listar usuários e seus posts:")
  users = session.query(User).join(User.posts).order_by(User.name).all()
  for user in users:
    print(f"Usuário: {user.name} ({user.email})")
    for post in user.posts:
      print(f"  - Post: {post.title}, Conteúdo: {post.content}")
