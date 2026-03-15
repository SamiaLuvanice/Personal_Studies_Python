name = input('Digite o seu nome:\n')

"""
- Arquivos:
1 - opção w - escrita, se o arquivo não existir ele é criado, se existir ele é sobrescrito
2 - opção a - escrita, se o arquivo não existir ele é criado, se existir ele é atualizado, ou seja, o conteúdo anterior é mantido e o novo conteúdo é adicionado ao final do arquivo
3 - opcao r - leitura, se o arquivo não existir ele gera um erro, se existir ele é lido
 """

 # Alternativa 1
# file = open('nome.txt', 'a')
# file.write(f"{name}\n")
# file.close()

#Alternativa 2
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
