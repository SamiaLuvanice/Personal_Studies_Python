from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()
app = Flask(__name__, instance_relative_config=True)

# Garantir que pasta instance existe
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'livros.sqlite3')
db.init_app(app)

from projeto import routes
from projeto.livro import Livro