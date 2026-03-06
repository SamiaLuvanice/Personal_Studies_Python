gameName = "Bomberman 23.0"

gameDescription = """
  Bomberman é um jogo de ação
  e estratégia onde os jogadores controlam
  personagens que colocam bombas para
  destruir obstáculos e inimigos.
  O objetivo é ser o último jogador sobrevivente ou
  completar objetivos específicos em cada fase.
"""

# string[início:fim] - indice começa na posição 0 | indice final -1

# 1 - Bucque toda string a partir da primeira posição
print(gameName[0:]) #Bomberman 23.0

# 2 - Busque toda string até a última posição
print(gameName[:9]) #Bomberman 23.0

# 3 - Busque toda string da terceira até a última posição
print(gameName[2:]) #mberman 23.0

"""
  string[início:fim:passo] - indice começa na posição 0 | indice final -1
"""
# 4 - Busque toda strign de 2 em 2 caracteres
print(gameName[::2]) #Boea 2.0

# 5 - Busque toda a string nos indices impares
print(gameName[1::2]) #oemn 30

# 6 - Busque toda a string de trás para frente
print(gameName[::-1]) #0.32 namreboB
