from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1- Contar itens de uma lista
#fruits = ["apple", "banana", "orange", "apple", "banana", "apple", "grape", "grape", "grape", "grape" ]
# print(Counter(fruits))

# 2 - Utilizando tupla nomeada
game = namedtuple('game', ['name', 'price', 'notes'])
g1 = game('The Last of Us', 150, 'Excelente jogo de ação e aventura')
g2 = game('God of War', 120, 'Jogo de ação e aventura com mitologia nórdica')
print(g1)
print(g2)

# 3 - Ordenando dicionários
students = [
  {'name': 'Alice', 'age': 25},
  {'name': 'Bob', 'age': 22},
  {'name': 'Charlie', 'age': 30}
]
students_sorted = sorted(students, key=itemgetter('age'))
print(students)
print(students_sorted)

# 4 - Utilizando fila ambas extremidades
deq = deque([1, 2, 3, 4, 5])
deq.appendleft(0)
print(deq)
deq.append(6)
print(deq)
deq.popleft()
print(deq)
deq.pop()
print(deq)
