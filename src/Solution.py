import Truck


class Solution:
    trucks: [Truck]
    totalDist: int
    totalRisque: int
    score: int

    def __init__(self, truckA: Truck, truckB: Truck, truckC: Truck):
        self.trucks.append(truckA)
        self.trucks.append(truckB)
        self.trucks.append(truckC)

    def calculateDistance(self) -> int:
        self.totalDist = 0
        for truck in self.trucks:
            self.totalDist += truck.getDistance()
        return self.totalDist

    def calculateRisque(self) -> int:
        self.totalRisque = self.trucks[0].getRisque() + self.trucks[1].getRisque() + self.trucks[2].getRisque()
        return self.totalRisque

    """
    La methode donne plusieurs poids au risque et à la distance totale et renvoie le score minimal
    """

    def calculateScore(self, weight: [int]) -> int:  # [0.3, 0.5, 0.7]
        scores = []
        for value in weight:
            scores.append(
                self.totalRisque * value + self.totalDist * (1 - value))  # TODO: Attention aux ordres de grandeur
        self.score = min(scores)
        return self.score

    def checkValidity(self) -> bool:  # La première et la dernière risquent d'être la banque
        towns = []
        for truck in self.trucks:
            for town in truck.getRoute():
                if town in towns:
                    return False
                else:
                    towns.append(town)
        return True
