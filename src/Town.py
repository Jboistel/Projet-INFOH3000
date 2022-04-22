class Town:
    name: str
    population: int

    def __init__(self, name, population):
        self.name = name
        self.population = population

    def getName(self):
        return self.name

    def getPop(self):
        return self.population

    def getCashAmount(self):
        return self.population * 0.7  # 0.7 is the tax/habitant
