import random

from numpy.random import randint

from Solution import *


class Generation:
    solutions: [Solution]
    data = Data()
    distMatrix = data.getDistMatrix()

    def __init__(self, solutions: [Solution]):
        self.solutions = solutions

    # Source : https://github.com/ralthor/GeneticAlgorithm-TSP/blob/feature-multi-tsp/src/algorithm.js
    def reproduce(self):
        newSolutions = []
        for i, solution in enumerate(self.solutions):
            if i != len(self.solutions) and i % 2 == 1:
                newSolutions.append(self.getChild(i, i + 1, True))
                newSolutions.append(self.getChild(i, i + 1, False))
        return Generation(newSolutions)

    # Source : https://github.com/ralthor/GeneticAlgorithm-TSP/blob/feature-multi-tsp/src/algorithm.js
    def getChild(self, x, y, forward):
        if forward:
            increment = +1
            rotate = 1
        else:
            increment = -1
            rotate = 0
        newcode = []
        px = deepcopy(self.solutions[x])
        py = deepcopy(self.solutions[y])
        current = px[randint(len(px))]  # Départ prit au hasard
        newcode.append(current)
        while px.length > 1:
            dx = px[-len(px) * rotate + px.index(current) + increment]  # Element suivant
            dy = py[-len(py) * rotate + py.index(current) + increment]
            px.pop(px.index(current))
            py.pop(py.index(current))
            # On choisi la ville la plus proche parmis les deux solutions
            # Encore besoin de faire une matrice des distance ou de trouver un équivalent
            current = dx if self.distMatrix[current][dx] < self.distMatrix[current][dy] else dy
            newcode.append(current)
        return Solution(newcode)

    def mutate(self):
        for solution in self.solutions:
            route = solution.getCode()
            if random.randint(0, 10) == 1:  # 10% de proba de mutation
                swapIndexA = random.randint(1, 19)
                swapIndexB = random.randint(1, 19)
                route[swapIndexA], route[swapIndexB] = route[swapIndexB], route[swapIndexA] # inversion de 2 elem au hasard
                newSol = Solution(route)
                if newSol.checkValidity():
                    solution = newSol

    def selection(self):
        self.solutions.sort(key=lambda s: s.calculateScore())
        self.solutions = self.solutions[:len(self.solutions) / 2]
