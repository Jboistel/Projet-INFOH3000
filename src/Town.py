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
