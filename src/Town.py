from __future__ import annotations
from Data import Data


class Town:
    name: str
    population: int
    id: int
    distancesToOthers = {}
    data: Data

    def __init__(self, id: int):
        self.id = id
        self.data = Data()
        self.population = self.data.getTownPop(id)
        self.name = self.data.getTownName(id)

    def getName(self) -> str:
        return self.name

    def getPop(self) -> int:
        return self.population

    def getCashAmount(self) -> float:
        return self.population * 0.7  # 0.7 is the tax/habitant

    def getDistanceToTown(self, other: Town) -> int:
        otherId = other.getId()
        distance = self.data.getDistMatrix()[self.id][otherId]
        return distance

    def getId(self) -> id:
        return self.id


def createTownsFromData():
    return [Town(i) for i in range(20)]


if __name__ == "__main__":
    towns = createTownsFromData()
    for town in towns:
        print("Nom: " + town.getName() +
              "\n\tId: " + str(town.getId()) +
              "\n\tPopulation: " + str(town.getPop()) +
              "\n\tCash: " + str(town.getCashAmount()) +
              "\n\tDistance to " + str(town.getId()-1) +
              ": " + str(town.data.getDistMatrix()[town.getId()][town.getId()-1]))
        assert town.getPop() * 0.7 == town.getCashAmount()

