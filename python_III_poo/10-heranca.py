class Animal:
    name = "" 
    size = ""
    color = ""

    def eat(self):
        print("O animal está comendo.")

class Horse(Animal):
    race = ""

    def escape(self):
        print("O cavalo está fugindo.")

class Lion(Animal):
    mane = True

    def hunt(self):
        print("O leão está caçando.")

h = Horse()
h.name = "Relâmpago"
h.race = "Puro Sangue"
h.color = "Vermelho"
h.escape()
h.eat()

l = Lion()
l.name = "Simba"
l.color = "Amarelo"
l.hunt()
l.eat()

print(f"O cavalo {h.name} é da raça {h.race} e tem a cor {h.color}.")
print(f"O leão {l.name} tem juba? {'Sim' if l.mane else 'Não'} e tem a cor {l.color}.")