# 1  - Fatorial de um número

"""
Fatorial de um número:
5! = 5 x 4 x 3 x 2 x 1 = 120
0! = 1
"""

def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n - 1)

number = int(input('Digite um número para calcular o fatorial: '))
print(f'O fatorial de {number} é: {factorial(number)}')

# 2 - Soma total de um número

"""
Soma total de um número:
5 = 5 + 4 + 3 + 2 + 1 = 15
"""

def total_sum(n):
  if n == 1:
    return 1
  else:
    return n + total_sum(n - 1)

number = int(input('Digite um número para calcular a soma total: '))
print(f'A soma total de {number} é: {total_sum(number)}')
