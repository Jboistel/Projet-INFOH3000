from random import randint
from Solution import *


class Generation:
    """Class to keep track of the evolution of the solutions of the problem,
    also responsible for the selection, crossover and mutation of solutions"""
    populationInitSize: int
    solutions: [Solution] = []
    data = Data()
    distMatrix = data.getDistMatrix()
    selectedForReproduction: [Solution] = []

    def __init__(self, solutions: [Solution]):
        self.solutions = solutions
        self.populationInitSize = len(solutions)

    def reproduce(self):
        """
        Uses a specific selection to choose 2 parents and make them reproduce to create a child solution.
        Source : https://github.com/ralthor/GeneticAlgorithm-TSP/blob/feature-multi-tsp/src/algorithm.js
        :return: a new Generation the same size of this one
        """
        forward = True
        newSolutions = []
        # self.elitismSelection()  # Goes with selectInElitePopulation
        newSolutions = self.steadyStateBasePopulation()  # Goes with steadyStateSelection
        while len(newSolutions) < self.populationInitSize:
            # parents = self.selectInElitePopulation()  # Goes with elitismSelection
            # parents = self.rouletteWheelSelection()
            parents = self.steadyStateSelection(newSolutions)  # Goes with steadyStateBasePopulation
            newSolution = self.getChild(parents[0], parents[1], forward)
            if newSolution:
                newSolutions.append(newSolution)
            forward = not forward
        return Generation(newSolutions)

    def getChild(self, x, y, forward):
        """
        Crossover between two parent as done in :
        https://github.com/ralthor/GeneticAlgorithm-TSP/blob/feature-multi-tsp/src/algorithm.js
        :param x: first parent
        :param y: second parent
        :param forward: way of iteration through parents code
        :return: new Solution, child of x and y
        """
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
        """
        Modify the population of this generation, each solution has 1/100 chance to mutate
        Mutation is a simple swap between two element of the code
        """
        for i, solution in enumerate(self.solutions):
            if random.randint(0, 100) == 1:  # 1% de proba de mutation
                didNotMutate = True
                while (didNotMutate):
                    route = deepcopy(solution.getCode())
                    swapIndexA = random.randint(0, 20)
                    swapIndexB = random.randint(0, 20)
                    route[swapIndexA], route[swapIndexB] = route[swapIndexB], route[swapIndexA]
                    # inversion de 2 elem au hasard
                    newSol = Solution(route)
                    if newSol.checkValidity():
                        self.solutions[i] = newSol
                        didNotMutate = False

    def elitismSelection(self):
        """
        Deletes the least effective half of the population in order to the best half to reproduce between them
        """
        self.solutions.sort(key=lambda s: s.calculateScore())
        self.solutions = self.solutions[:len(self.solutions) // 2]

    def selectInElitePopulation(self):
        """
        Chooses 2 random solutions to reproduce in a selected elite population
        :return: 2 solutions
        """
        return random.choices(self.solutions, k=2)

    def rouletteWheelSelection(self):
        """
        Chooses two solutions to reproduce through a random weighted choice, weight is 1 over the solution score
        :return: two solution to reproduce
        """
        return random.choices(self.solutions, weights=[1 / solution.score for solution in self.solutions], k=2)

    def steadyStateBasePopulation(self):
        """
        :return: the best half of this generation population as a base for next generation solution
        """
        self.solutions.sort(key=lambda s: s.calculateScore())
        return self.solutions[:len(self.solutions) // 2]

    def steadyStateSelection(self, population):
        """
        Chooses 2 random solutions to reproduce in a base steady state population
        :param population: the base population
        :return: a new solution for the popultion
        """
        return random.choices(population, k=2)

    def isSolutionOptimal(self, optiSol: Solution) -> bool:
        """
        Compares a solution to every solution in the generation to determine if it is dominant or not
        :param optiSol: the solution to compare to the population
        :return: True if the solution is dominant, False else
        """
        for solution in self.solutions:
            solDist = solution.getTotalDistance()
            optidist = optiSol.getTotalDistance()
            solRisk = solution.getTotalRisk()
            optiRisk = optiSol.getTotalRisk()
            if solution != optiSol and ((solDist < optidist and solRisk < optiRisk)
                                        or (solDist == optidist and solRisk < optiRisk)
                                        or (solDist < optidist and solRisk == optiRisk)):
                return False
        return True

    def areSolutionsEquivalent(self, sol1: Solution, sol2: Solution) -> bool:
        """
        Compare two solution to know if they're equivalent
        :return: True if the two solutions are equivalent, False else
        """
        if sol1 == sol2:
            return True
        routes1 = []
        routes2 = []
        for truck in sol1.trucks:
            routes1.append(truck.getRouteIds())
        for truck in sol2.trucks:
            routes2.append(truck.getRouteIds())

        if (routes1[0] in routes2) and (routes1[1] in routes2) and (routes1[2] in routes2):
            return True
        else:
            return False

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


if __name__ == "__main__":  # Tests for the class
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
    while len(children) < 100:
        child = gen.getChild(gen.solutions[0], gen.solutions[1], True)
        if child:
            children.append(child)

    print(children)

    children2 = []
    while len(children2) < 100:
        child = gen.getChild(gen.solutions[0], gen.solutions[1], False)
        if child:
            children2.append(child)

    import matplotlib.pyplot as plt



    distancesParents = [i.totalDist for i in gen.getSolutions()]
    risquesParents = [i.totalRisk for i in gen.getSolutions()]
    distancesEnfants = [i.totalDist for i in children]
    distancesEnfants2 = [i.totalDist for i in children2]
    risquesEnfants = [i.totalRisk for i in children]
    risquesEnfants2 = [i.totalRisk for i in children2]
    plt.ylabel("Distance")
    plt.xlabel("Risque")
    plt.title("Enfants générés par deux parents")
    plt.scatter(risquesParents, distancesParents, marker=".")
    plt.scatter(risquesEnfants, distancesEnfants, marker="v")
    plt.scatter(risquesEnfants2, distancesEnfants2, marker="^")
    plt.show()
