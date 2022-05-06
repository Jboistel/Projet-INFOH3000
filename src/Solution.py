from Data import Data
from copy import deepcopy

from Truck import *


class Solution:
    trucks: [Truck] = []
    totalDist: int
    totalRisque: int
    score: int
    code: [] #somme des routes ?
    data = Data()

    def __init__(self, code):
        self.code = code
        self.decode(code)

    def calculateDistance(self) -> int:
        self.totalDist = 0
        for truck in self.trucks:
            self.totalDist += truck.getDistance()
        return self.totalDist

    def calculateRisque(self) -> int:
        self.totalRisque = self.trucks[0].getRisque() + self.trucks[1].getRisque() + self.trucks[2].getRisque()
        return self.totalRisque

    """
    La methode donne plusieurs poids au risque et à la distance totale et renvoie le score minimal
    """

    def calculateScore(self, weight: [int]) -> int:  # [0.3, 0.5, 0.7]
        scores = []
        for value in weight:
            scores.append(
                self.totalRisque * value + self.totalDist * (1 - value))  # TODO: Attention aux ordres de grandeur
        self.score = min(scores)
        return self.score

    def checkDuplicates(self) -> bool:  # La première et la dernière risquent d'être la banque
        towns = []
        for truck in self.trucks:
            for town in truck.getRoute():
                if (town in towns) and (town.getName() != "bank"):
                    return True
                else:
                    towns.append(town)
        return False

    def checkValidity(self) -> bool:
        for truck in self.trucks:
            truckRouteId = truck.getRoute().getId()
            if (((1 in truckRouteId) and (4 in truckRouteId)) #vérifie qu'un camion ne passe pas par 2 des 3 communes les plus peuplées
                    or ((1 in truckRouteId) and (15 in truckRouteId))
                    or ((4 in truckRouteId) and (15 in truckRouteId))):
                return False
            if truck.getAmount() > sum(self.data.getNbPeople())/2: #vérifie qu'un camion ne contienne pas plus de la moitié du montant total à collecter
                return False
        return True

    def decode(self, code: [int]):
        codeCopy = deepcopy(code)
        for i in range(3):
            route = [codeCopy.pop(0)]
            while (len(codeCopy) != 0) and codeCopy[0] != 0:
                route.append(codeCopy.pop(0))
            if (route[0] != 0): route.insert(0,0)
            if (route[-1] != 0): route.append(0)
            self.trucks.append(Truck(route))

    """
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
    """

    def getCode(self):
        return self.code
