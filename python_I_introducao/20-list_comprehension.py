# 1 - Liste valores de 0 a 10 que sejam menor do que 4.
#for i in range(10):
#  if i < 4:
#    print(i)

listNumbers = [i for i in range(10) if i < 4]
print(listNumbers)

gamesList = ['GTA', 'FIFA', 'MARIO', 'ZELDA', 'CALL OF DUTY', 'FORTNITE']

# 2 - Jogos que possuam a letra A.
newList = [x for x in gamesList if 'A' in x]
print(newList)

# 3 - Jogos que eu zerei.
gamesFinished = [ x for x in gamesList if x != 'ZELDA']
print(gamesFinished)
