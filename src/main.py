from copy import deepcopy
from Data import Data
from Solution import Solution
from Generation import Generation
import matplotlib.pyplot as plt
import random

solutions: [Solution] = []

global code
code = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 0]


def plot(sols: [Solution], it):
    distances: [float] = []
    risks: [float] = []
    for solution in sols:
        distances.append(solution.getTotalDistance())
        risks.append(solution.getTotalRisk())
    plt.ylabel("Distance")
    plt.xlabel("Risque")
    plt.title("Solution " + str(it))
    plt.scatter(risks, distances)
    plt.show()


def generateSolution():
    # codeCopy = deepcopy(code)
    codeCopy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 0]
    random.shuffle(codeCopy)
    # print(code)
    sol = Solution(codeCopy)
    i = 0

    while not sol.checkValidity() and i < 10000:
        random.shuffle(codeCopy)
        sol = Solution(codeCopy)
        i += 1

    if sol.checkValidity():
        return sol
    else:
        return
    """if not sol.checkValidity():
        generateSolution()
    else:
        return sol"""


def algo(nbSolInit: int, nbIterations: int):
    """"
    1- création premieres solutions
    2- boucle sur X itérations de : -selection()
                                    -reproduce()
                                    -mutate()
    """
    global solutions

    for i in range(nbSolInit):  # on génère un premier échantillon de 20 solutions au hasard
        solutions.append(generateSolution())
        # print(solutions[i].code) # debug

    gen = Generation(solutions)

    gen_list = []
    for i in range(nbIterations):
        gen_list.append(gen)
        gen.selection()
        gen = gen.reproduce()
        gen.mutate()  # Mutation à faire dans la reproduction
        print(len(gen_list))
    plot(gen_list[0].getSolutions(), "start")
    plot(gen_list[-1].getSolutions(), "end")
    plot(getParetoFrontier(gen), "pareto")
    # plot(gen.getSolutions())


def getParetoFrontier(gen: Generation):
    optiSols = []
    for solution in gen.getSolutions():
        if (gen.isSolutionOptimal(solution)):
            optiSols.append(solution)
    return optiSols


def main():
    data = Data()
    algo(nbSolInit=1000, nbIterations=10)
    # print(len(solutions))
    # plot(solutions)
    # for solution in solutions:
    #    print(solution)


if __name__ == "__main__":
    main()
