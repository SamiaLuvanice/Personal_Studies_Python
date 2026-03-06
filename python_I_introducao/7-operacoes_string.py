gameDescription = """
  Bomberman é um jogo de ação
  e estratégia onde os jogadores controlam
  personagens que colocam bombas para
  destruir obstáculos e inimigos.
  O objetivo é ser o último jogador sobrevivente ou
  completar objetivos específicos em cada fase.
"""

gameName = "Bomberman"
gameVersion = "23.0"
line = "+"

# 1 - Operação de concatenação de strings
print(line * 25)
gameFullName = gameName + gameVersion
print(gameFullName)

# 2 - Operação de multiplicação de strings
print(line * 25)

# 3 - Procura paaçvra dentro de um texto
print("bomb" in gameDescription) #Retorna True ou False
