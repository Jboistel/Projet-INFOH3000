from Solution import *
import matplotlib.pyplot as plt
from CheckSolutions import lineToInfoConverter


def grapheSolution(s: Solution, number: int):
    cols = ["yellow", "orange", "red"]

    plt.title("Solution " + str(number) + "\nCode: " + str(s.getCode()))
    for t, truck in enumerate(s.trucks):
        tournee = [(c.position[0], c.position[1]) for c in truck.route]
        for i in range(len(tournee) - 1):
            plt.arrow(tournee[i][0], tournee[i][1],
                      tournee[i + 1][0] - tournee[i][0], tournee[i + 1][1] - tournee[i][1],
                      length_includes_head=True, color=cols[t])
    plt.show()


if __name__ == "__main__":
    with open("src/solutionsPareto.csv") as file:
        file.readline()
        for i, line in enumerate(file):
            info = lineToInfoConverter(line)
            grapheSolution(Solution(info[2]), i)
