"""
1 - O métdo de classe utiliza o parametro referente a classe.
2 - Pode acessar ou modificar o estado da classe.
3 - Usamos o decorador @classmethod para criar um método de classe.
"""

class Console:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall("é \w*", string)
        name = item[0][2:]
        price = float(item[1][2:])
        return cls(name, price)

wiiU = Console.from_text("O console é Wii U e o preço é 1500 reais")
xbox = Console.from_text("O console é Xbox e o preço é 1200 reais")

print(wiiU.name)
print(wiiU.__dict__) # O dicionário de atributos do objeto wiiU, mostrando os atributos name e price.
print(xbox.name)
print(xbox.__dict__)
