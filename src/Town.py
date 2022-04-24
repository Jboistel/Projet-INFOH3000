class Town:
    name: str
    population: int
    distancesToOthers = {}

    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def getName(self):
        return self.name

    def getPop(self):
        return self.population

    def getCashAmount(self):
        return self.population * 0.7  # 0.7 is the tax/habitant

    def getDistanceToTown(self, other):
        return self.distancesToOthers[other]
