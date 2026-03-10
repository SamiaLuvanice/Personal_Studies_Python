import random
# 1 - Seleciona valor aleatorio de uma lista
fruits = ["apple", "banana", "orange", "grape"]
print(random.choice(fruits))

# 2 - Gera um número aleatório em um intervalo
print(random.randint(1, 10))

# 3 - Seleciona caracteres aleatórios de uma string
name = "Sâmia Luvanice"
r2 = random.choice(name)
print(r2)

# 4 - Seleciona mais de um valor aletória
# Sintaxe random.sample(sequencia, tamanho)
print(random.sample(fruits, 2))
print(random.sample(name, 5))
