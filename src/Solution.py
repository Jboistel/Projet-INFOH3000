import Truck


class Solution:
    trucks: [Truck]
    score: int

    def __init__(self, truckA, truckB, truckC):
        self.trucks.append(truckA)
        self.trucks.append(truckB)
        self.trucks.append(truckC)

    def calculateScore(self):
        # TODO
        return self.score
