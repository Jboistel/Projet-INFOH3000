from copy import deepcopy

from Truck import *


class Solution:
    trucks: [Truck]
    totalDist: int
    totalRisque: int
    score: int
    code: []

    def __init__(self, code):
        self.code = code
        self.decode(code)

    def calculateDistance(self):
        self.totalDist = 0
        for truck in self.trucks:
            self.totalDist += truck.getDistance()
        return self.totalDist

    def calculateRisque(self):
        self.totalRisque = self.trucks[0].getRisque() + self.trucks[1].getRisque() + self.trucks[2].getRisque()
        return self.totalRisque

    def calculateScore(self, weight: [int]):  # [0.3, 0.5, 0.7]
        scores = []
        for value in weight:
            scores.append(
                self.totalRisque * value + self.totalDist * (1 - value))  # TODO: Attention aux ordres de grandeur
        self.score = min(scores)
        return self.score

    def checkValidity(self):  # La première et la dernière risquent d'être la banque
        towns = []
        for truck in self.trucks:
            for town in truck.getRoute():
                if town in towns:
                    return False
                else:
                    towns.append(town)
        return True

    def decode(self, code: [int]):
        codeCopy = deepcopy(code)
        sortedCode = []
        start = codeCopy.index(0)
        while len(codeCopy) > start:
            sortedCode.append(codeCopy.pop(start))
        for i in range(len(codeCopy)):
            sortedCode.append(codeCopy.pop(0))
        for i in range(3):
            route = [sortedCode.pop(0)]
            while sortedCode[0] != 0:
                route.append(sortedCode.pop(0))
            self.trucks.append(Truck(route))
