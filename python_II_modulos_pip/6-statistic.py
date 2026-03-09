import statistics

# 1 - Aplicar a média
print(statistics.mean([1, 2, 3, 4, 5]))

# 2 - Aplicar a mediana
print(statistics.median([1, 4, 3, 9, 5]))
print(statistics.median([1, 4, 3, 9]))

# 3 - Aplicar a moda
print(statistics.mode([1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1]))

# 4- Desvio padrão
"""
 - Desvio padrão é uma medida de dispersão que indica o quanto os valores de um conjunto de dados estão afastados da média.
 - Quanto maior o desvio padrão, mais os valores estão dispersos em relação à média.
"""
print(statistics.stdev([1, 2, 3, 4, 5]))
