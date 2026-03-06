# 1 - Função de potência de números
power = lambda num: num ** 2

# 2  -Função que verifica se o número é par
pair = lambda num: num % 2 == 0

# 3 - Função que divide um número por outro
divNum = lambda x, y : x / y

# 4 - Função que inverte uma string
reverse = lambda s: s[::-1]

# Testando as funções
print(power(5))  # Output: 25
print(power(9)) # Output: 81

print(pair(4))  # Output: True
print(pair(7))  # Output: False

print(divNum(10, 2))  # Output: 5.0
print(divNum(6, 3))  # Output: 2.0

print(reverse("Hello"))  # Output: "olleH"
print(reverse("Python"))  # Output: "nohtyP"
