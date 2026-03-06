# 1 - Cálculo da distancia e valor da passagem
distance = float(input("Digite a distância a percorrer em km\n"))
if distance <= 200:
  ticket = distance * 0.50
else:
  ticket = distance * 0.35
print(f"O valor da passagem é: R${ticket:.2f}")

# 2 - Aumento de salário do funcionário
salary = float(input("Digite o salário do funcionário\n"))
perc_increase = 0.15 if salary > 1250 else 0.10
new_salary = salary *  perc_increase
print(f"Seu aumento será de : R${new_salary:.2f}")
