# Substituindo caractere repetido

name = input("Digite o nome do jogo: ")
char = name[0].lower()  # Pegando o primeiro caractere e convertendo para minúsculo
new_name = name.replace(char, "$")
new_name = char + new_name[1:]

print(new_name)

# Troca de caracteres

st1 = "abc"
st2 = "xyz"

new_st1 = st2[:2] + st1[2:]
new_st2 = st1[:2] + st2[2:]

print("String 1:", new_st1)
print("String 2:", new_st2)
