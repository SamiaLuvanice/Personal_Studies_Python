class Movie:
    name = ""
    yearLaunch = 0
    includedInPlan = False
    note = 0
    durationMinutes = 0

# Primeiro Filme
movie = Movie()
movie.name = "Super Mario Bros"
movie.yearLaunch = 2023
movie.includedInPlan = False
movie.note = 8.5
movie.durationMinutes = 120

print("##Dados do Filme##")
print(f"Nome: {movie.name}")
print(f"Ano de Lançamento: {movie.yearLaunch}")
print(f"Incluído no Plano: {movie.includedInPlan}")
print(f"Nota: {movie.note}")
print(f"Duração: {movie.durationMinutes} minutos")