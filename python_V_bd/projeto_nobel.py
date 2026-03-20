import requests 
from pymongo import MongoClient

# 1 - Estabelece conexão com o mongodb
client = MongoClient()

db= client['nobel']

# 2 - Importar os dados em documentos
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
api_endpoints = {'prize': ('prize', 'prizes'), 'laureate': ('laureate', 'laureates')}
for collection_name, json_key in api_endpoints.items():
    url = f'https://api.nobelprize.org/v1/{json_key[0]}.json'
    print(f'Acessando: {url}')
    response = requests.get(url, headers=headers)
    
    print(f'Status Code: {response.status_code}')
    response.raise_for_status()  # Lança erro se status >= 400
    documents = response.json()
    collection = db[collection_name]
    collection.insert_many(documents[json_key[1]])

# 3 - Acessando coleções / Contagem de documentos 
prizes = db['prize']
laureates = db['laureate']

len_prizes = prizes.count_documents({})
len_laureates = laureates.count_documents({})

print(f'Número de prêmios: {len_prizes}')
print(f'Número de laureados: {len_laureates}')
