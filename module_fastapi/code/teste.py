from fastapi import FastAPI

app = FastAPI()

# localhost:8000/
@app.get("/")
def inicio():
    return {"message": "Olá, mundo!"}
