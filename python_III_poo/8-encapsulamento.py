class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary # Atributo privado, não pode ser acessado diretamente fora da classe.

    def show(self):
        print(f"Funcionário: {self.name}, Salário: {self.__salary}")

fulano = Employee("Fulano", 3000)
sicrano = Employee("Sicrano", 4000)

fulano.show()
sicrano.show()

fulano.__salary = 40000
fulano.show()