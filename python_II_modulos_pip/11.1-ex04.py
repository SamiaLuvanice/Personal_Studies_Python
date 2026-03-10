import random

done = False

while not done:
  print("O que você deseja fazer?")
  print("1 - Adicionar um número")
  print("2 - Sair")

  choice = input("Escolha uma opção: ")

  if choice == "1":
    print(f"Advinhe um número de 1 a 100\n")
    number = int(input("Digite seu palpite: "))
    result = random.randint(1, 100)
    if number == result:
      print("Parabéns! Você acertou!")
    else:
      print(f"Errado! O número correto era {result}. Tente novamente!")

  elif choice == "2":
    done = True

  else:
    print("Opção inválida. Por favor, escolha 1 ou 2.")

print("Obrigado por jogar! Até a próxima!")
