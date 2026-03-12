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
    
    def techinicalSheet(self):
        print("#### Ficha Técnica ####")
        print(f"Nome: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Incluído no Plano: {'Sim' if self.includedInPlan else 'Não'}")
        print(f"Nota: {self.note}")
        print(f"Duração: {self.durationMinutes} minutos")

mario = Movie("Super Mario Bros", 1993, False, 5.5, 104)
top_gun = Movie("Top Gun: Maverick", 2022, True, 8.5, 130)
mario.techinicalSheet()
top_gun.techinicalSheet()