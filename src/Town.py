from __future__ import annotations


class Town:
    name: str
    population: int
    distancesToOthers = {}

    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population

    def getName(self) -> str:
        return self.name

    def getPop(self) -> int:
        return self.population

    def getCashAmount(self) -> float:
        return self.population * 0.7  # 0.7 is the tax/habitant

    def getDistanceToTown(self, other: Town) -> int:
        return self.distancesToOthers[other]
