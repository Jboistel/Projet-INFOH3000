import random
from Data import Data
from Town import Town
from copy import deepcopy

from Truck import Truck


class Solution:
    """Represents a specific solution to the problem with the 3 trucks being the 3 salesmen. Each solution has its own
    risk, distance, score and code, the code is the genome of the solution"""
    trucks: [Truck] = []
    mutated = False
    totalDist: int = 0
    totalRisk: int = 0
    score: int = 0
    code: []
    data = Data()

    def __init__(self, code, mutated=False):
        self.code = code
        self.trucks = []
        self.mutated = mutated
        self.decode(code)
        self.calculateRisk()
        self.calculateDistance()
        self.calculateScore()

    def calculateDistance(self) -> float:
        """Returns the total distance traveled for this solution"""
        self.totalDist = 0
        for truck in self.trucks:
            self.totalDist += truck.getDistance()
        self.totalDist = round(self.totalDist, 3)
        return self.totalDist

    def getTotalDistance(self) -> float:
        return self.totalDist

    def calculateRisk(self) -> int:
        """Returns the total risk took for this solution"""
        self.totalRisk = round((self.trucks[0].getRisk() + self.trucks[1].getRisk() + self.trucks[2].getRisk()), 3)
        return self.totalRisk

    def getTotalRisk(self) -> float:
        return self.totalRisk

    def calculateScore(self, weights=None) -> int:
        """Computes the score of the solution by comparing several possible scores and keeping the best (lowest).
        This gives a chance for solution with either high distance and low rick or low distance and high risk to carry
        on their genome.
        Risk and distance are normalized by their approximated order of magnitude"""
        if weights is None:
            weights = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
        scores = []
        normalised_risk = self.totalRisk / 50000000
        normalised_dist = self.totalDist / 200
        for value in weights:
            scores.append(
                normalised_risk * value + normalised_dist * (1 - value))
        self.score = min(scores)
        return self.score

    def checkDuplicates(self) -> bool:
        """Check if a solution has a duplication of town in its trucks route"""
        towns = []
        for truck in self.trucks:
            for town in truck.getRoute():
                if (town in towns) and (town.getName() != "bank"):
                    return True
                else:
                    towns.append(town)
        return False

    def checkValidity(self) -> bool:
        """Ckecks validity of a solution:
        No truck should contain more that 50% of the total money
        No truck should stop at the 3 most populated town (1, 4 and 15)"""
        for truck in self.trucks:
            truckRouteIds = truck.getRouteIds()
            if (1 in truckRouteIds) and (4 in truckRouteIds) and (15 in truckRouteIds):
                return False
            if truck.getTotalAmount() > sum(
                    self.data.getNbPeople()) * 0.7 / 2:
                return False
        return True

    def decode(self, code: [int]):
        """Translates the code to 3 trucks for the solution"""
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


if __name__ == "__main__":  # Test for the class
    baseCode = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 0]
    random.shuffle(baseCode)
    codeCpy = deepcopy(baseCode)
    sol = Solution(codeCpy)
    testDecode(sol)
    testCheckValidityAndDuplicates()
    testComputeDistanceRiskAndScores()
