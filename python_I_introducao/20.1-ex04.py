# Lançamento do Foguete
import winsound

x = 10
while x >= 0:
    print(x)
    x -= 1
winsound.Beep(2500, 500)  # Frequência de 2500 Hz por 500 ms

# Tabuada de um número
number = int(input("Digite um número para ver sua tabuada: "))
begin = int(input("Digite o início da tabuada: "))
end = int(input("Digite o fim da tabuada: "))

x = begin
while x <= end:
    print(f"{number} x {x} = {number * x}")
    x += 1
