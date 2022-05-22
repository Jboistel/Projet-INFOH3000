from Town import Town


class Truck:
    """Represents one travelling salesman in the solution to the problem,
       It has a specific route, a 'real-time' amount of money transported for risk computation,
       and the total amount transported"""
    route: [Town]
    amount: int
    totalAmount: int

    def __init__(self, route: [Town]):
        self.route = route
        self.amount = 0
        self.calculateTotalAmount()

    def calculateTotalAmount(self):
        """Computes the total amount of money transported"""
        self.totalAmount = 0
        for town in self.route:
            self.totalAmount += town.getCashAmount()

    def getRoute(self) -> [Town]:
        return self.route

    def getRouteIds(self) -> [int]:
        return [town.getId() for town in self.route]

    def getDistance(self) -> int:
        """Computes and returns the total distance traveled by this truck"""
        result = 0
        for i in range(len(self.route) - 1):
            result += self.route[i].getDistanceToTown(self.route[i + 1])
        return result

    def getAmount(self) -> float:
        return self.amount

    def getTotalAmount(self) -> float:
        return self.totalAmount

    def increaseAmount(self, town: Town):
        self.amount += town.getCashAmount()

    def getRisk(self) -> float:
        """Computes the total risk took by this Truck"""
        amount = 0
        result = 0
        for i in range(len(self.route) - 1):
            amount += self.route[i].getCashAmount()
            result += amount * self.route[i].getDistanceToTown(self.route[i + 1])
            self.increaseAmount(self.route[i])
        amount += self.route[-1].getCashAmount()
        result += amount * self.route[-1].getDistanceToTown(self.route[0])
        return result


def testRoute():
    from random import shuffle
    from copy import deepcopy
    routeSrc = [Town(i) for i in range(20)]
    shuffle(routeSrc)
    truck = Truck(deepcopy(routeSrc))
    for i in range(len(routeSrc)):
        assert truck.getRoute()[i].getName() == routeSrc[i].getName()
    print("Route test passed")


def testAmount():
    from random import randint
    routeSrc = [Town(randint(0, 19)) for _ in range(5)]
    truck = Truck(routeSrc)
    totalExpected = 0
    for i in truck.getRoute():
        assert truck.getAmount() == totalExpected
        truck.increaseAmount(i)
        totalExpected += i.getCashAmount()
    assert totalExpected == truck.getAmount()
    print("Amount test passed")


def testDistance():
    from random import randint
    routeSrc = [Town(randint(0, 19)) for _ in range(5)]
    truck = Truck(routeSrc)
    expectedDist = routeSrc[0].getDistanceToTown(routeSrc[1]) + \
                   routeSrc[1].getDistanceToTown(routeSrc[2]) + \
                   routeSrc[2].getDistanceToTown(routeSrc[3]) + \
                   routeSrc[3].getDistanceToTown(routeSrc[4])
    assert expectedDist == truck.getDistance()
    print("Distance test passed")


def testRisque():
    from random import randint
    routeSrc = [Town(randint(0, 19)) for _ in range(5)]
    truck = Truck(routeSrc)
    expectedRisque = 0
    expectedAmount = 0
    for i in range(len(routeSrc) - 1):
        expectedAmount += routeSrc[i].getCashAmount()
        expectedRisque += routeSrc[i].getDistanceToTown(routeSrc[i + 1]) * expectedAmount
    expectedAmount += routeSrc[-1].getCashAmount()
    expectedRisque += routeSrc[-1].getDistanceToTown(routeSrc[0]) * expectedAmount
    assert expectedRisque == truck.getRisk()
    print("Risque test passed")


if __name__ == "__main__":  # Tests for this class
    testRoute()
    testAmount()
    testDistance()
    testRisque()
