num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Operadores aritméticos
soma = num1 + num2
sub = num1 - num2
div = num1 / num2
mult = num1 * num2
mod = num1 % num2
exp = num1 ** num2

print(f"Soma: {soma}")
print(f"Subtração: {sub}")
print(f"Divisão: {div}")
print(f"Multiplicação: {mult}")
print(f"Módulo: {mod}")
print(f"Exponenciação: {exp}")

# Operadores de comparação
bigger = num1 > num2
smaller = num1 < num2
equal = num1 == num2
diferent = num1 != num2
bigger_equal = num1 >= num2
smaller_equal = num1 <= num2

print(f"Igual: {equal}")
print(f"Diferente: {diferent}")
print(f"Maior: {bigger}")
print(f"Menor: {smaller}")
print(f"Maior ou igual: {bigger_equal}")
print(f"Menor ou igual: {smaller_equal}")

#Operadores de atribuição
num1 += 1  # num1 = num1 + 1
num1 -= 1  # num1 = num1 - 1
num1 *= 1  # num1 = num1 * 1
num1 /= 1  # num1 = num1 / 1
print(f"num1 após incremento: {num1}")
print(f"num2 após decremento: {num2}")
print(f"num1 após multiplicação: {num1}")
print(f"num1 após divisão: {num1}")
