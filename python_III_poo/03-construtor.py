class Movie:
    def __init__(self, name, yearLaunch, includedInPlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedInPlan = includedInPlan
        self.note = note
        self.durationMinutes = durationMinutes
    
    # Método para representar o objeto como string
    def __str__(self):
        return f"Filme: {self.name}"

# Primeiro Filme
movie = Movie("Super Mario Bros", 2023, False, 8.5, 120)
movie2 = Movie("Batman", 2023, False, 8.5, 120)

print(f"Nome: {movie.name}")
print(f"Nome: {movie2.name}")
print(movie)  # Isso irá chamar o método __str__ e imprimir "Filme: Super Mario Bros"
print(movie2)  # Isso irá chamar o método __str__ e imprimir "Filme: Batman"