from Data import Data
from Solution import Solution
from Generation import Generation
import matplotlib.pyplot as plt
import random
import csv

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
    plt.xlim(30, 140)
    plt.ylim(40, 150)
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
    global solutions

    for i in range(nbSolInit):  # on génère un premier échantillon de 20 solutions au hasard
        solutions.append(generateSolution())
        # print(solutions[i].code) # debug

    gen_list = []
    for i in range(nbIterations):
        gen = Generation(solutions)

        gen.selection()
        gen.reproduce()
        gen.mutate()  # Mutation à faire dans la reproduction

        solutions = gen.getSolutions()
        gen_list.append(gen)
        print(str(round((len(gen_list) / nbIterations) * 100, 2)) + '%')
        # print(len(gen.getSolutions()))
    plot(gen_list[0].getSolutions(), "start")
    plot(gen_list[-1].getSolutions(), "end")
    plot(getParetoFrontier(gen), "pareto")
    # plot(gen.getSolutions())
    export(gen.getSolutions())


def getParetoFrontier(gen: Generation):
    optiSols = []
    for solution in gen.getSolutions():
        if (gen.isSolutionOptimal(solution)):
            optiSols.append(solution)
    return optiSols


def export(sols: [Solution]):
    with open('solutions.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Distance', 'Risque', 'Solution'])
        for solution in sols:
            writer.writerow([solution.getTotalDistance(), solution.getTotalRisk(), solution.getCode()])


def main():
    algo(nbSolInit=100, nbIterations=100)


if __name__ == "__main__":
    main()
