from Solution import *
import matplotlib.pyplot as plt
from CheckSolutions import lineToInfoConverter


def grapheSolution(s: Solution, number: int):
    """
    Creates a visual graph of the given solution
    :param s: the solution to graph
    :param number: n° of the solution in a set if applicable
    """
    cols = ["gold", "orange", "red"]

    plt.title("Solution " + str(number) + " Distance=" + str(s.totalDist) + ", Risque=" + str(s.totalRisk) + "\nCode: " + str(s.getCode()))
    for t, truck in enumerate(s.trucks):
        tournee = [(c.position[0], c.position[1]) for c in truck.route]
        for i in range(len(tournee) - 1):
            plt.arrow(tournee[i][0], tournee[i][1],
                      tournee[i + 1][0] - tournee[i][0], tournee[i + 1][1] - tournee[i][1],
                      length_includes_head=True, color=cols[t])
    plt.show()


if __name__ == "__main__":
    with open("solutionsPareto.csv") as file:
        file.readline()
        for i, line in enumerate(file):
            info = lineToInfoConverter(line)
            grapheSolution(Solution(info[2]), i)
