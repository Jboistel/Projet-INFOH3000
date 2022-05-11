from Data import Data
from Town import Town
from copy import deepcopy

from Truck import Truck


class Solution:
    trucks: [Truck] = []
    totalDist: int = 0
    totalRisk: int = 0
    score: int = 0
    code: []  # somme des routes ?
    data = Data()

    def __init__(self, code):
        self.code = code
        self.trucks = []
        self.decode(code)
        self.calculateRisk()
        self.calculateDistance()
        self.calculateScore()

    def calculateDistance(self) -> float:
        self.totalDist = 0
        for truck in self.trucks:
            self.totalDist += truck.getDistance()
        return self.totalDist

    def getTotalDistance(self) -> float:
        return round(self.totalDist, 2)

    def calculateRisk(self) -> int:
        self.totalRisk = (self.trucks[0].getRisk() + self.trucks[1].getRisk() + self.trucks[2].getRisk()) / (
            200000)
        return self.totalRisk

    def getTotalRisk(self) -> float:
        return round(self.totalRisk, 2)

    """
    La methode donne plusieurs poids au risque et à la distance totale et renvoie le score minimal
    """

    def calculateScore(self, weights=None) -> int:  #
        if weights is None:
            # weights = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]
            weights = [0.3, 0.5, 0.7]
        scores = []
        for value in weights:
            scores.append(
                self.totalRisk * value + self.totalDist * (1 - value))  # TODO: Attention aux ordres de grandeur
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

    def checkValidity(self) -> bool:  # TODO
        for truck in self.trucks:
            truckRouteIds = truck.getRouteIds()
            if (((1 in truckRouteIds) and (
                    4 in truckRouteIds))  # vérifie qu'un camion ne passe pas par 2 des 3 communes les plus peuplées
                    or ((1 in truckRouteIds) and (15 in truckRouteIds))
                    or ((4 in truckRouteIds) and (15 in truckRouteIds))):
                return False
            if truck.getAmount() > sum(
                    self.data.getNbPeople()) / 2:  # vérifie qu'un camion ne contienne pas plus de la moitié du montant total à collecter
                return False

        return True

    def decode(self, code: [int]):
        codeCopy = deepcopy(code)
        for i in range(3):
            route = []
            if len(codeCopy) != 0:
                routeIds = [codeCopy.pop(0)]
                while (len(codeCopy) != 0) and codeCopy[0] != 0:
                    routeIds.append(codeCopy.pop(0))
                if routeIds[0] != 0 or len(routeIds) == 1:  # on ajoute 0 au début de la liste
                    routeIds.insert(0, 0)
                if routeIds[-1] != 0:  # on ajoute 0 à la fin de la liste
                    routeIds.append(0)

                for townId in routeIds:
                    route.append(Town(townId))
            else:
                route = [Town(0), Town(0)]
            self.trucks.append(Truck(route))

    """Peut etre utile pour le check validity ?
    def decode(self, code: [int]):
        c = deepcopy(code)
        i = c.index(0)
        a = c[:i]  # premier camion
        c = c[i + 1:]
        i = c.index(0)
        b = c[:i]  # deuxieme camion
        c = c[i + 1:]  # troisieme camion
    """

    def getCode(self):
        return self.code
