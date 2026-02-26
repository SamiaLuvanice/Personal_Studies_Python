import pprint

gamesDict = {
    'resident evil 4': {
        'yearLaunch': 2024,
        'classification': 9.5,
        'genre': ['action', 'survival horror']
    },
    'mario adyssey': {
        'yearLaunch': 2017,
        'classification': 9.0,
        'genre': ['action', 'adventure']
    },
    'the last of us part 2': {
        'yearLaunch': 2020,
        'classification': 9.8,
        'genre': ['action', 'adventure']
    }
}

pp = pprint.PrettyPrinter(depth=4)
pp.pprint(gamesDict)

# 1 - Buscar informações dentro de um dicionário aninhado
print(gamesDict['resident evil 4']['genre'])

# 2 - Adicionar um novo item
gamesDict['the legend of zelda: breath of the wild'] = {
    'yearLaunch': 2017,
    'classification': 9.7,
    'genre': ['action', 'adventure']
}
pp.pprint(gamesDict)

# 3 - Excluir um item
del gamesDict['mario adyssey']
pp.pprint(gamesDict)
