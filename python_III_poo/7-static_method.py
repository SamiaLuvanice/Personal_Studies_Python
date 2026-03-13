"""
1 - O método estático não utiliza o parâmetro referente a classe.
2 - Pode acessar ou modificar o estado da classe.
3 - Usamos o decorador @staticmethod para criar um método estático. 
"""

class Course:
    def __init__(self, name, trail):
        self.name = name
        self.trail = trail

    @staticmethod
    def course_trail(trail):
        if trail == "Python Fundamentos":
            courses = ["Dominando o Python", "Módulos e Pip", "Órientação a Objetos"]
        elif trail == "Automação com o Python":
            courses = ["Automação com o Python", "Web Scraping", "Assistente Virtual"]
        else: 
            courses = ["A definir"]
        return courses

print(Course.course_trail("Python Fundamentos"))
print(Course.course_trail("Automação com o Python"))
print(Course.course_trail("Data Science com o Python"))