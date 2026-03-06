gameFifa = {
    'name': 'FIFA 2024',
    'yearLauch': 2024,
    'gamePrice': 90.50,
    'classification': 8.5,
    'genre': ['Esporte', 'Família']
}
print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

# 1 - Recuperar um elemnto do dicionario
print(gameFifa['genre'])
print(gameFifa.get('classification'))

# 2- Buscar apenas as chaves do dicionário
print(gameFifa.keys())

# 3 - Buscar apenas os valores do dicionário
print(gameFifa.values())

# 4 - Buscar os itens do dicionário com chave e valor
print(gameFifa.items())

# 5 - Adicionar itens no dicionário
gameFifa['players'] = 2
print(gameFifa)

# 6 - Arualizar itens no dicionário
gameFifa.update({'players': 1})
print(gameFifa)

# 7- Remover itens do dicionário
gameFifa.pop('players')
print(gameFifa)
