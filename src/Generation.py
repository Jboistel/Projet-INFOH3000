import random

from random import randint

from Solution import *


class Generation:
    populationInitSize: int
    solutions: [Solution] = []
    data = Data()
    distMatrix = data.getDistMatrix()
    selectedForReproduction: [Solution] = []

    def __init__(self, solutions: [Solution]):
        self.solutions = solutions
        self.populationInitSize = len(solutions)

    # Source : https://github.com/ralthor/GeneticAlgorithm-TSP/blob/feature-multi-tsp/src/algorithm.js
    def reproduce(self):
        forward = True
        newSolutions = []
        # newSolutions = self.elitismSelection()  # Goes with selectInElitePopulation
        newSolutions = self.steadyStateBasePopulation()  # Goes with steadyStateSelection
        while len(newSolutions) < self.populationInitSize:
            # parents = self.selectInElitePopulation(newSolutions)  # Goes with elitismSelection
            # parents = self.rouletteWheelSelection()
            parents = self.steadyStateSelection(newSolutions)  # Goes with steadyStateBasePopulation
            newSolution = self.getChild(parents[0], parents[1], forward)
            if newSolution:
                newSolutions.append(newSolution)
            if forward:
                forward = not forward
            else:
                forward = not forward
        return Generation(newSolutions)

    # Source : https://github.com/ralthor/GeneticAlgorithm-TSP/blob/feature-multi-tsp/src/algorithm.js
    def getChild(self, x, y, forward):
        if forward:
            increment = +1
            rotate = 1
        else:
            increment = -1
            rotate = 0
        ret: Solution
        tries = 0
        while tries < 20:
            tries += 1
            newcode = []
            px = deepcopy(x)
            py = deepcopy(y)
            pxCode = px.getCode()
            pyCode = py.getCode()
            current = pxCode[randint(0, len(pxCode) - 1)]  # Départ prit au hasard
            newcode.append(current)
            while len(pxCode) > 1:
                dx = pxCode[-len(pxCode) * rotate + pxCode.index(current) + increment]  # Element suivant
                dy = pyCode[-len(pyCode) * rotate + pyCode.index(current) + increment]
                pxCode.pop(pxCode.index(current))
                pyCode.pop(pyCode.index(current))
                # On choisi la ville la plus proche parmis les deux solutions
                # Encore besoin de faire une matrice des distance ou de trouver un équivalent
                current = dx if self.distMatrix[current][dx] < self.distMatrix[current][dy] and \
                                self.distMatrix[current][dx] != 0 else dy
                newcode.append(current)
            ret = Solution(newcode)
            if ret.checkValidity():
                return ret
        return

    def mutate(self):
        for i, solution in enumerate(self.solutions):
            route = solution.getCode()
            if random.randint(0, 100) == 1:  # 1% de proba de mutation
                swapIndexA = random.randint(0, 20)
                swapIndexB = random.randint(0, 20)
                route[swapIndexA], route[swapIndexB] = route[swapIndexB], route[
                    swapIndexA]  # inversion de 2 elem au hasard
                newSol = Solution(route)
                if newSol.checkValidity():
                    self.solutions[i] = newSol

    def elitismSelection(self):
        self.solutions.sort(key=lambda s: s.calculateScore())
        newSolutions = self.solutions[:len(self.solutions) // 2]
        return newSolutions

    def selectInElitePopulation(self, newSolutions):  # Peut avoir une répétition
        return random.choices(newSolutions, k=2)

    def rouletteWheelSelection(self):
        return random.choices(self.solutions, weights=[1 / solution.score for solution in self.solutions], k=2)

    def steadyStateBasePopulation(self):
        self.solutions.sort(key=lambda s: s.calculateScore())
        return self.solutions[:len(self.solutions) // 2]

    def steadyStateSelection(self, population):
        return random.choices(population, k=2)

    def isSolutionOptimal(self, optiSol: Solution):
        for solution in self.solutions:
            if solution != optiSol and (solution.getTotalDistance() < optiSol.getTotalDistance()
                                        and solution.getTotalRisk() < optiSol.getTotalRisk()):
                return False
        return True

    def getSolutions(self) -> [Solution]:
        return self.solutions


def testOptimalSolutionAndSelection():
    bestSol = Solution([12, 5, 1, 9, 4, 0, 15, 11, 13, 17, 7, 19, 2, 3, 10, 14, 18, 8, 0, 6, 16])
    print(bestSol.totalDist, bestSol.totalRisk)

    avgSol = Solution([12, 17, 7, 1, 13, 11, 14, 3, 19, 18, 6, 10, 2, 5, 4, 0, 16, 9, 8, 15, 0])
    print(avgSol.totalDist, avgSol.totalRisk)

    baddestSol = Solution([17, 5, 7, 14, 19, 11, 18, 0, 12, 9, 0, 15, 8, 13, 6, 2, 4, 1, 10, 3, 16])
    print(baddestSol.totalDist, baddestSol.totalRisk)

    gen = Generation([bestSol, avgSol, avgSol, baddestSol])
    assert gen.isSolutionOptimal(bestSol)
    assert gen.isSolutionOptimal(avgSol)
    assert not gen.isSolutionOptimal(baddestSol)
    print("Optimal Solution selection test passed")
    testSelection(gen)


def testSelection(gen):
    gen.elitismSelection()
    assert len(gen.getSolutions()) == 2
    print("Selection test passed")


if __name__ == "__main__":
    sol1 = Solution([5, 18, 19, 2, 17, 16, 7, 13, 9, 0, 14, 15, 6, 0, 10, 8, 3, 1, 11, 12, 4])
    sol2 = Solution([10, 8, 3, 1, 11, 12, 4, 0, 14, 15, 6, 0, 5, 18, 19, 2, 17, 16, 7, 13, 9])
    sol3 = Solution([17, 10, 19, 18, 6, 15, 0, 0, 11, 2, 8, 3, 1, 9, 4, 14, 5, 7, 16, 13, 12])
    sol4 = Solution([3, 2, 19, 12, 1, 15, 14, 0, 6, 0, 13, 17, 11, 18, 4, 10, 5, 7, 16, 8, 9])

    print("Dist : " + str(sol1.calculateDistance()) + " Risk : " + str(sol1.calculateRisk()))
    print("Dist : " + str(sol2.calculateDistance()) + " Risk : " + str(sol2.calculateRisk()))
    print("Dist : " + str(sol3.calculateDistance()) + " Risk : " + str(sol3.calculateRisk()))
    print("Dist : " + str(sol4.calculateDistance()) + " Risk : " + str(sol4.calculateRisk()))

    """
    testOptimalSolutionAndSelection()

    baseCode = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 0]
    random.shuffle(baseCode)
    codeCpy = deepcopy(baseCode)
    sol = Solution(codeCpy)
    random.shuffle(baseCode)
    codeCpy = deepcopy(baseCode)
    sol2 = Solution(codeCpy)

    gen = Generation([sol, sol2])

    children = []
    for i in range(100):
        children.append(gen.getChild(0, 1, True))

    children2 = []
    for i in range(100):
        children2.append(gen.getChild(0, 1, False))

    import matplotlib.pyplot as plt

    distancesParents = [i.totalDist for i in gen.getSolutions()]
    risquesParents = [i.totalRisk for i in gen.getSolutions()]
    distancesEnfants = [i.totalDist for i in children]
    distancesEnfants2 = [i.totalDist for i in children2]
    risquesEnfants = [i.totalRisk for i in children]
    risquesEnfants2 = [i.totalRisk for i in children2]
    plt.ylabel("Distance")
    plt.xlabel("Risque")
    plt.title("Solution")
    plt.scatter(risquesParents, distancesParents, marker=".")
    plt.scatter(risquesEnfants, distancesEnfants, marker="v")
    plt.scatter(risquesEnfants2, distancesEnfants2, marker="^")
    plt.show()
    """
