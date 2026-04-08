from fastapi import FastAPI, HTTPException

app = FastAPI()

cursos = {	 
    1: {
        "nome": "Dominando o Python",
        "nivel": "básico",
        "formacao": "Python Fundamentos"
    },
    2: {
        "nome": "Automação de Tarefas",
        "nivel": "intermediário",
        "formacao": "Automação"
    },
    3: {
        "nome": "Automação com Selenium",
        "nível": "intermediário",
        "formacao": "Automação"
    }

}

# Path parameters
@app.get("/cursos/{formacao}")
async def get_cursos_formacao(formacao: str):
    cursos_formacao = [
    curso for curso in cursos.values()
    if curso["formacao"].lower() == formacao.lower()
    ]
    return cursos_formacao

#Query parameters
@app.get("/cursos/")
async def get_cursos_formacao_query(formacao: str):
    cursos_formacao = [
    curso for curso in cursos.values()
    if curso["formacao"].lower() == formacao.lower()
    ]
    if not cursos_formacao:
        raise HTTPException(
            status_code=404, 
            detail="Nenhum curso encontrado para a formação especificada.")
    return cursos_formacao