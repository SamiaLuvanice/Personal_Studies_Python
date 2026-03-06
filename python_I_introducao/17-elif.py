num1 = float(input("Digite o primeiro número\n"))
num2 = float(input("Digite o segundo número\n"))
operation = input("Digite a operação desejada (soma, subtração, multiplicação ou divisão)\n")

if operation == "soma":
    result = num1 + num2
    print(f"O resultado da soma é: {result}")
elif operation == "subtração":
    result = num1 - num2
    print(f"O resultado da subtração é: {result}")
elif operation == "multiplicação":
    result = num1 * num2
    print(f"O resultado da multiplicação é: {result}")
elif operation == "divisão":
    if num2 != 0:
        result = num1 / num2
        print(f"O resultado da divisão é: {result}")
    else:
        print("Não é possível dividir por zero.")
else:
    print("Operação inválida. Por favor, escolha entre soma, subtração, multiplicação ou divisão.")
