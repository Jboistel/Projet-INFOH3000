import random
from math import floor

from Data import Data
from Town import Town
from copy import deepcopy

from Truck import Truck

global lowWeight, midWeight, highWeight

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
            self.totalDist += truck.getDistance() / 200
        self.totalDist = round(self.totalDist, 3)
        return self.totalDist

    def getTotalDistance(self) -> float:
        return self.totalDist

    def calculateRisk(self) -> int:
        self.totalRisk = round((self.trucks[0].getRisk() + self.trucks[1].getRisk() + self.trucks[2].getRisk()) / (
                100000 * 500), 3)
        return self.totalRisk

    def getTotalRisk(self) -> float:
        return self.totalRisk

    """
    La methode donne plusieurs poids au risque et à la distance totale et renvoie le score minimal
    """

    def calculateScore(self, weights=None) -> int:
        if weights is None:
            weights = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        scores = []
        for value in weights:
            scores.append(
                self.totalRisk * value + self.totalDist * (1 - value))  # TODO: Attention aux ordres de grandeur
        self.score = min(scores)
        """for value in weights:
            self.score += self.totalDist * value + self.totalDist * (1 - value)"""
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
            truckRouteIds = truck.getRouteIds()
            if (1 in truckRouteIds) and (
                    4 in truckRouteIds) and (15 in truckRouteIds):  # vérifie qu'un camion ne passe pas par 2 des 3 communes les plus peuplées
                return False
            if truck.getAmount() > sum(
                    self.data.getNbPeople()) * 0.7 / 2:  # vérifie qu'un camion ne contienne pas plus de la moitié du montant total à collecter
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


def testDecode(solution: Solution):
    dest = []
    expected = [0, 0, 0, 0, 0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    for truck in solution.trucks:
        assert truck.getRouteIds()[0] == 0
        assert truck.getRouteIds()[-1] == 0
        for townId in truck.getRouteIds():
            dest.append(townId)
    dest.sort()
    for i in range(len(dest)):
        assert expected[i] == dest[i]
    print("Decode test passed")


def testCheckValidityAndDuplicates():
    goodCode = [1, 2, 3, 5, 6, 0, 4, 7, 8, 9, 10, 11, 0, 12, 13, 14, 15, 16, 17, 18, 19]
    solution = Solution(goodCode)
    assert solution.checkValidity()
    badCode1 = [1, 4, 15, 0, 2, 3, 5, 6, 7, 8, 9, 10, 0, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    solution = Solution(badCode1)
    assert not solution.checkValidity()
    badCode2 = [1, 0, 4, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    solution = Solution(badCode2)
    assert not solution.checkValidity()
    badCode3 = [1, 1, 0, 1, 0, 2, 2]
    solution = Solution(badCode3)
    assert not solution.checkDuplicates()
    print("Check Validity test passed")


def testComputeDistanceRiskAndScores():
    baseCode = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 0]
    random.shuffle(baseCode)
    codeCpy = deepcopy(baseCode)
    sol = Solution(codeCpy)
    expectedDist = sol.trucks[0].getDistance() + sol.trucks[1].getDistance() + sol.trucks[2].getDistance()
    expectedDist /= 200
    expectedDist = round(expectedDist, 3)
    assert sol.calculateDistance() == expectedDist
    expectedRisk = sol.trucks[0].getRisk() + sol.trucks[1].getRisk() + sol.trucks[2].getRisk()
    expectedRisk /= 30000000
    expectedRisk = round(expectedRisk, 3)
    assert sol.calculateRisk() == expectedRisk
    expectedScore = min(expectedRisk * 0.3 + expectedDist * (1 - 0.3),
                        expectedRisk * 0.5 + expectedDist * (1 - 0.5),
                        expectedRisk * 0.7 + expectedDist * (1 - 0.7))
    assert sol.calculateScore([0.3, 0.5, 0.7]) == expectedScore
    print("Computing Distance and Risk test passed")


if __name__ == "__main__":
    baseCode = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 0]
    random.shuffle(baseCode)
    codeCpy = deepcopy(baseCode)
    sol = Solution(codeCpy)
    testDecode(sol)
    testCheckValidityAndDuplicates()
    testComputeDistanceRiskAndScores()
