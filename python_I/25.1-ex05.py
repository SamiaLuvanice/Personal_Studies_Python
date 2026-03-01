# 1 -  Verifica letra maiúscula e minúscula
def check_char(text):
  type = {"Uppercase": 0, "Lowercase": 0}
  for char in text:
    if char.isupper():
      type["Uppercase"] += 1
    elif char.islower():
      type["Lowercase"] += 1
  print("Texto original:", text)
  print("Número de letras maiúsculas:", type["Uppercase"])
  print("Número de letras minúsculas:", type["Lowercase"])

check_char("Hello World!")

# 2 - Verifica número par ou impar
def check_numbers(numbers):
  pair = []
  odd = []
  for number in numbers:
    if number % 2 == 0:
      pair.append(number)
    else:
      odd.append(number)
  return pair, odd
print(check_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
