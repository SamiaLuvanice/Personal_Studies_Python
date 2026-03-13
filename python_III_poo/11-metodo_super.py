class Phone:
    def __init__(self, brand, model_name, price):
        self._brand = brand
        self._model_name = model_name
        self._price = price

    def __str__(self):
        return f"Brand: {self._brand}, Model: {self._model_name}"
    
    @staticmethod
    def make_a_call(phone_number):
        print(f"Lihando para {phone_number}...")

class Smartphone(Phone):
    def __init__(self, brand, model_name, price, ram, internal_memory, back_camera):
        super().__init__(brand, model_name, price) # Chama o construtor da classe pai (Phone) para inicializar os atributos herdados.
        self.ram = ram
        self.internal_memory = internal_memory
        self.back_camera = back_camera

Moto = Phone("Motorola", "G9 Plus", 1500)
print(Moto)
Moto.make_a_call("11999999999")
print(f"Valor do {Moto._brand} {Moto._model_name}: R${Moto._price}")
print(vars(Moto))

Iphone = Smartphone("Apple", "iPhone 12", 5000, "4GB", "128GB", "12MP")
print(Iphone)
Iphone.make_a_call("11988888888")
print(f"Valor do {Iphone._brand} {Iphone._model_name}: R${Iphone._price}")
print(f"RAM: {Iphone.ram}, Memória Interna: {Iphone.internal_memory}, Câmera Traseira: {Iphone.back_camera}")