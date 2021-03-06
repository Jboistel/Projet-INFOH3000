from Data import Data
from Solution import *
from Generation import Generation
import matplotlib.pyplot as plt
import random
import csv
import time

solutions: [Solution] = []


def plot(sols: [Solution], it):
    """
    Plot every solution given in a pyplot plot
    :param sols: solutions to plot
    :param it: n° of the iteration
    """
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
    """
    Used for multiple population in one plot
    :param sols: population to plot this time
    :param symbol: used for this population
    """
    distances = [solution.getTotalDistance() for solution in sols]
    risques = [solution.getTotalRisk() for solution in sols]
    plt.scatter(risques, distances, marker=symbol)


def plotFront(solutionsOnFront: [Solution]):
    risks = [sol.totalRisk for sol in solutionsOnFront]
    dists = [sol.totalDist for sol in solutionsOnFront]
    plt.plot(risks, dists)


def generateSolution():
    """
    Generate a random base solution
    :return: a solution
    """
    codeCopy = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0, 0]
    random.shuffle(codeCopy)
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
        print(str(round(i / nbIterations * 100, 2)) + "%")
    gen_list.append(gen)
    pareto = getParetoFront(gen)
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
    export('solutions.csv', gen.getSolutions())
    export('solutionsPareto.csv', pareto)


def getParetoFront(gen: Generation):
    """
    :param gen: last generation of the algorithm
    :return: the Pareto front of the problem
    """
    optiSols = []
    for sol1 in gen.getSolutions():
        isOpti = True
        for optiSol in optiSols:
            if gen.areSolutionsEquivalent(sol1, optiSol):
                isOpti = False
        if isOpti and gen.isSolutionOptimal(sol1):
            optiSols.append(sol1)
    return optiSols


def export(file, sols: [Solution]):
    """
    Writes given solution in file in a CSV format
    :param file: the file where the solutions are to be writen
    :param sols: solutions to write
    """
    with open(file, 'w', encoding='UTF8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Distance', 'Risque', 'Solution'])
        for solution in sols:
            writer.writerow([solution.getTotalDistance(), solution.getTotalRisk(), solution.getCode()])


def main():
    tic = time.perf_counter()
    algo(nbSolInit=1000, nbIterations=10)
    toc = time.perf_counter()
    print(f"Algo in {toc - tic:0.4f} seconds")


if __name__ == "__main__":
    main()
