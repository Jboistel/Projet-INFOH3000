from Data import Data
from Solution import *
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

def plotThis(sols, symbol):
    distances = [solution.getTotalDistance() for solution in sols]
    risques = [solution.getTotalRisk() for solution in sols]
    plt.scatter(risques, distances, marker=symbol)

def plotFront(solutionsOnFront: [Solution]):
    risks = [sol.totalRisk for sol in solutionsOnFront]
    dists = [sol.totalDist for sol in solutionsOnFront]
    plt.plot(risks, dists)


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
    gen_list.append(gen)
    for i in range(nbIterations):
        gen = gen.reproduce()
        gen.mutate()  # Mutation à faire dans la reproduction
        print(i)
    gen_list.append(gen)
    """plot(gen_list[0].getSolutions(), "start")
    plot(gen_list[-1].getSolutions(), "end")
    plot(getParetoFrontier(gen), "pareto")"""
    pareto = getParetoFrontier(gen)
    for sol in pareto:
        print(sol.score)
    plt.ylabel("Distance")
    plt.xlabel("Risque")
    plotThis(gen_list[0].getSolutions(), "^")
    plotThis(gen_list[-1].getSolutions(), "v")
    plotThis(pareto, ".")
    plt.show()
    plt.ylabel("Distance")
    plt.xlabel("Risque")
    plotThis(pareto, ".")
    pareto.sort(key=lambda s: s.totalRisk)
    plotFront(pareto)
    plt.show()
    # plot(gen.getSolutions())
    if input("Voulez-vous sauvegarder? (Y:N): ") == "Y":
        export(pareto)


def getParetoFrontier(gen: Generation):
    optiSols = []
    for solution in gen.getSolutions():
        if gen.isSolutionOptimal(solution):
            optiSols.append(solution)
    return optiSols


def export(sols: [Solution]):
    with open('solutions.csv', 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Distance', 'Risque', 'Solution'])
        for solution in sols:
            writer.writerow([solution.getTotalDistance(), solution.getTotalRisk(), solution.getCode()])


def main():
    algo(nbSolInit=1000, nbIterations=10)




if __name__ == "__main__":
    main()
