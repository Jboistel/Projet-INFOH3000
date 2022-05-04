from Data import Data
import Solution
import matplotlib.pyplot as plt

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


if __name__ == "__main__":
    main()
