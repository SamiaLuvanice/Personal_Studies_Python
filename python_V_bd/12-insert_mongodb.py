from pymongo import MongoClient

cliente = MongoClient()

mydb = cliente.obcblog
mycol = mydb.posts

post1 = {
    "title": "My third post",
    "category": "FastAPI",
    "author": {
        "name": "Teste 2",
        "email": "teste2@example.com"
    }
}

result = mycol.insert_one(post1)
print("Post inserted with id:", result.inserted_id)