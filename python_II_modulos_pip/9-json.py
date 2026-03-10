import json

# 1 - Strings para Dicionários
person = '{"name": "Sâmia", "languages": ["Python", "JavaScript"]}'
person_dictionary = json.loads(person)
print(person_dictionary)
print(person_dictionary['languages'])

# 2 - Dicionários para Json
person_json = json.dumps(person_dictionary)
print(person_json)
print(type(person_json))
print(type(person_dictionary))

# 3 - Formatando json
print(json.dumps(person_dictionary, indent=4, sort_keys=True))

# 4  -  Salvando jsone m txt
with open('person.txt', 'w') as json_file:
  json.dump(person_dictionary, json_file)

# 5 - Lendo json de txt
with open('person.txt', 'r') as json_file:
  person_dictionary = json.load(json_file)
  print(person_dictionary)
