name = input("Digite o nome do jogo:\n")
yearLauch = int(input("Digite o ano de lançamento do jogo:\n"))
gamePrice = float(input("Digite o preço do jogo:\n"))
planeIncluded = bool(input("O jogo inclui um plano de assinatura? (True/False):\n"))

print("### Dados do Jogo ###")
print("======================")
# Alternativa 1
# print("Nome do Jogo:", name)
# print("Ano de Lançamento:", yearLauch)
# print("Preço do Jogo:", gamePrice)
# print("Inclui Plano de Assinatura?", planeIncluded)

#Alternativa 2
# print("Nome do Jogo:", name, "\nAno de Lançamento:", yearLauch,
#       "\nPreço do Jogo:", gamePrice, "\nInclui Plano de Assinatura?", planeIncluded)

#Alternativa 3
print(f"Nome do Jogo: {name}")
print(f"Ano de Lançamento: {yearLauch}")
print(f"Preço do Jogo: {gamePrice}")
print(f"Inclui Plano de Assinatura? {planeIncluded}")
