import math

# 1 - Acessar o número pi
print(math.pi)
print(f"{math.pi:.2f}")  # Imprime o número pi com 2 casas decimais

# 2 - Acessar o número Euler
print(math.e)
print(f"{math.e:.2f}")  # Imprime o número Euler com 2 casas decimais

# 3- Arredondar um número para cima e para baixo
num1 = 10.4

print(math.ceil(num1))  # Arredonda para cima
print(math.floor(num1))  # Arredonda para baixo

# 4 - Fatorial de um número
num2 = int(input("Digite um número para calcular o fatorial: "))
print(math.factorial(num2))  # Calcula o fatorial de num2

# 5 - Potência de um número
print(math.pow(2, 3))  # Calcula 2 elevado a 3

# 6 - Raiz quadrada de um número
print(math.sqrt(169))  # Calcula a raiz quadrada de 169

# 7 - MDC de dois números
num3 = int(input("Digite o primeiro número para calcular o MDC: "))
num4 = int(input("Digite o segundo número para calcular o MDC: "))
print(math.gcd(num3, num4))  # Calcula o MDC de num3 e num4

# 8 - Logaritmo de um número
print(math.log(100, 10))  # Calcula o logaritmo de 100 na base 10
