from Data import Data
from Solution import Solution
from Generation import Generation
import matplotlib.pyplot as plt
import random


solutions: [Solution] = []
global code
code = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 0]


def plot(sols: [Solution]):
    distances: [float] = []
    risques: [float] = []
    for solution in sols:
        distances.append(solution.calculateDistance())
        risques.append(solution.calculateRisque())
    plt.ylabel("Distance")
    plt.xlabel("Risque")
    plt.scatter(distances, risques)
    plt.show()


def generateSolution():
    random.shuffle(code)
    #print(code)
    sol = Solution(code)

    if not sol.checkValidity():
        generateSolution()
    else:
        return sol


def algo(nbSolInit: int, nbIterations: int):
    """"
    1- création premieres solutions
    2- boucle sur X itérations de : -selection()
                                    -reproduce()
                                    -mutate()
    """

    for i in range(nbSolInit):  # on génère un premier échantillon de 20 solutions au hasard
        solutions.append(generateSolution())
        #print(solutions[i].code) # debug

    gen = Generation(solutions)

    """"
    for i in range(nbIterations):
        gen.selection()
        gen.reproduce()
        gen.mutate()
        # plot(gen.getSolutions())
    """


def main():
    data = Data()
    algo(nbSolInit=20, nbIterations= 50)
    print(len(solutions))
    #plot(solutions)
    for solution in solutions:
        print(solution.code)


    """
    list = [3, 0, 5, 6, 0, 1, 2, 4]
    print(list[-len(list)])
    new = []
    current = list[randint(len(list))]
    print("Start: ", current)
    new.append(current)
    while len(list) > 1:
        dx = list[-len(list) + list.index(current) + 1]
        print(dx)
        list.pop(list.index(current))
        current = dx
        new.append(current)
        print(new)
"""


if __name__ == "__main__":
    main()
