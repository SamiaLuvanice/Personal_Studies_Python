import re

text = "OneBitCode: Transformamos pessoas comuns em programadores extraordinários"

# 1- Índice inicial e final de palavras
# O r significa que estamos trabalhando com uma string raw, ou seja, uma string que não processa caracteres de escape

match = re.search(r"comuns", text)
print('Índice inicial:', match.start())  # Índice inicial da palavra "comuns"
print('Índice final:', match.end())  # Índice final da palavra "comuns"

# 2 - Buscando o índice que possui o ponto final
site = "www.onebitcode.com.br"
match = re.search(r"\.", site)  # O \. é necessário para escapar o
print('Índice do ponto final:', match.start())  # Índice do ponto final

# 3 - Buscando uma lista de caracteres dentro de uma frase
pattern = r"[a-m]"  # Busca por letras de a a m
result = re.findall(pattern, text)
print(text)
print('Letras de a a m:', result)

# 4 - Verificando o início de uma string
rule = r'^A'
phrase = ["A OneBitCode é a melhor", "OneBitCode é a melhor", "A melhor escola de programação do Brasil"]
for f in phrase:
    if re.search(rule, f):
        print(f'"{f}" começa com a letra A')
    else:
        print(f'"{f}" não começa com a letra A')

# 5 - Verificando o final de uma string
rule_end = r'!$'
phrase_end = ["OneBitCode é a melhor!", "OneBitCode é a melhor", "A melhor escola de programação do Brasil!"]
for f in phrase_end:
    if re.search(rule_end, f):
        print(f'"{f}" termina com um ponto de exclamação')
    else:
        print(f'"{f}" não termina com um ponto de exclamação')
