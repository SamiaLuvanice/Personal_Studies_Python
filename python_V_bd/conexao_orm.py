from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

user = 'postgres'
password = 'xxxx'
host = 'localhost'
port = '5433'
database = 'blog'

DATABASE_URI = f'postgresql://{user}:{password}@{host}:{port}/{database}'

engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
