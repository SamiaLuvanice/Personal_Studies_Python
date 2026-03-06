"""
*args - Utilzamos ele quando não temos certeza de quantos argumentos serão passados na função, ou seja,
quando queremos passar uma quantidade variável de argumentos para uma função.
 - Os argumentos são passados como uma tupla, então eles são imutáveis.

 **kwargs - Utilizamos ele quando não temos certeza de quantos argumentos nomeados serão passados na função,
 ou seja, quando queremos passar uma quantidade variável de argumentos nomeados para uma função.
 - Os argumentos são passados como um dicionário, então eles são mutáveis.
"""

# 1 - Soma de números
def sum(*num):
  sum_total = 0
  for n in num:
    sum_total += n
  print(f"A soma dos números é: {sum_total}")
sum(4, 5)

# 2 - Apresentação de cursos
def presentation(**data):
  for key, value in data.items():
    print(f"O curso de {key} tem {value} alunos.")

presentation(Python=30, Java=25, JavaScript=20)
