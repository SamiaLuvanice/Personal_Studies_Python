class Employee:
    def __init__(self, name, salary):
        self.name = name # Atributo público, pode ser acessado diretamente fora da classe.
        self.__salary = salary # Atributo privado, não pode ser acessado diretamente fora da classe.

    def show(self):
        print(f"Funcionário: {self.name}, Salário: {self.__salary}")

    # Método para buscar dados
    def get_salary(self):
        return self.__salary

    # Método para modificar atriibuto privado
    def set_salary(self, salary):
        self.__salary = salary

fulano = Employee("Fulano", 3000)
sicrano = Employee("Sicrano", 4000)

fulano.show()
sicrano.show()

fulano.name = "Fulano da Silva"

fulano.show()
sicrano.show()

fulano.set_salary(50000)
fulano.show()
