class Animal:
        def __init__(self, name, category):
                self.name = name
                self.category = category

class Fish(Animal):
    race = ""

class Parrots(Animal):
    color = ""

class Zoo:
    def __init__(self):
        self.animals = {}

    def add_animal(self, animal):
        if not isinstance(animal, Animal):
            raise TypeError("Somente objetos do tipo Animal podem ser adicionados")
        self.animals[animal.name] = animal

    def total_of_category(self, category):
        result = 0
        for animal in self.animals.values():
            if animal.category == category:
                result += 1
        return f"Total de animais na categoria {category}: {result}"

zoo = Zoo()

fish1 = Fish("Nemo", "Fish")
print(vars(fish1))

parrot1 = Parrots("Polly", "Parrot")
print(vars(parrot1))

zoo.add_animal(fish1)
zoo.add_animal(parrot1)

print(zoo.total_of_category("Fish"))
print(zoo.total_of_category("Parrot"))
