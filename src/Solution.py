from Data import Data
from Town import Town
from copy import deepcopy

from Truck import Truck


class Solution:
    trucks: [Truck] = []
    totalDist: int = 0
    totalRisque: int = 0
    score: int = 0
    code: []  # somme des routes ?
    data = Data()

    def __init__(self, code):
        self.code = code
        self.trucks = []
        self.decode(code)
        self.calculateRisque()
        self.calculateDistance()
        self.calculateScore()

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

    def calculateScore(self, weights: [int] = [0.3, 0.5, 0.7]) -> int:  #
        scores = []
        for value in weights:
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
        """
        for truck in self.trucks:
            truckRouteIds = truck.getRouteIds()
            if (((1 in truckRouteIds) and (4 in truckRouteIds)) #vérifie qu'un camion ne passe pas par 2 des 3 communes les plus peuplées
                    or ((1 in truckRouteIds) and (15 in truckRouteIds))
                    or ((4 in truckRouteIds) and (15 in truckRouteIds))):
                return False
            if truck.getAmount() > sum(self.data.getNbPeople())/2: #vérifie qu'un camion ne contienne pas plus de la moitié du montant total à collecter
                return False
        """
        return True

    def decode(self, code: [int]):
        route = []
        codeCopy = deepcopy(code)
        for i in range(3):
            if len(codeCopy) != 0:
                routeIds = [codeCopy.pop(0)]
                while (len(codeCopy) != 0) and codeCopy[0] != 0:
                    routeIds.append(codeCopy.pop(0))
                if routeIds[0] != 0:  # on ajoute 0 au début de la liste
                    routeIds.insert(0, 0)
                if routeIds[-1] != 0:  # on ajoute 0 à la fin de la liste
                    routeIds.append(0)

                for townId in routeIds:
                    route.append(Town(townId))
            else:
                route = [Town(0), Town(0)]
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
            route.append(0)
            self.trucks.append(Truck(route))
    """

    def getCode(self):
        return self.code
