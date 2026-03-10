import hashlib

# 1 - Verificar os algoritmos disponíveis
#print(hashlib.algorithms_available)

# 2 - Algoritmos disponíveis de acordo com o SO
#print(hashlib.algorithms_guaranteed)

# 3 - Utilizando o sha256
algorithm = hashlib.sha256(b'Hello World')
print(algorithm.hexdigest())

# 4 - Utilizando o md5
algorithm = hashlib.md5(b'Hello World')
print(algorithm.hexdigest())
