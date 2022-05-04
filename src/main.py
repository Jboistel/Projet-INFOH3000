from Data import Data
import Solution
import matplotlib.pyplot as plt
from numpy.random import randint

global distances
distances = {}

solutions: Solution


def plot():
    distances: float
    risques: float
    for solution in solutions:
        distances += solution.calculateDistance()
        risques += solution.calculateRisque()
    plt.ylabel("Distance")
    plt.xlabel("Risque")
    plt.scatter(distances, risques)
    plt.show()


def main():
    data = Data()
    print(data.getDistMatrix())
    plot()

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


if __name__ == "__main__":
    main()
