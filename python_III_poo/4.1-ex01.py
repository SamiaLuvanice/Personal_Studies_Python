class Movie:
    def __init__(self, name, yearLaunch, includedInPlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedInPlan = includedInPlan
        self.totalEvaluation = 0
        self.durationMinutes = durationMinutes
        self.evaluators = 0

    # Método para representar o objeto como string
    def __str__(self):
        return f"Filme: {self.name}"

    def techinicalSheet(self):
        print("#### Ficha Técnica ####")
        print(f"Nome: {self.name}")
        print(f"Ano de Lançamento: {self.yearLaunch}")
        print(f"Incluído no Plano: {'Sim' if self.includedInPlan else 'Não'}")
        print(f"Nota: {self.totalEvaluation}")
        print(f"Duração: {self.durationMinutes}")
        print(f"Total de Avaliações: {self.evaluators}\n")

    def evaluate(self, note):
        self.totalEvaluation += note
        self.evaluators += 1

    def average(self):
        print(f"Média do filme {self.name}: {self.totalEvaluation / self.evaluators}")
        print(f"Total de Avaliações: {self.evaluators}\n")

mario = Movie("Super Mario Bros", 1993, False, 104)
avatar = Movie("Avatar", 2009, True, 162)

mario.evaluate(8)
mario.evaluate(9)
mario.average()
avatar.evaluate(10)
avatar.evaluate(9)
avatar.average()
