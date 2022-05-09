import Town


class Truck:
    route: [Town]
    amount: int

    def __init__(self, route: [Town]):
        self.route = route
        self.amount = 0

    def getAmount(self) -> float:
        self.amount = 0
        for town in self.route:
            self.amount += town.getCashAmount()
        return self.amount

    def getRoute(self) -> [Town]:
        return self.route

    def getRouteIds(self) -> [int]:
        route = []
        for town in self.route:
            route.append(town.getId())
        return route

    def increaseAmount(self, town: Town):
        self.amount += town.getCashAmount()

    def getDistance(self) -> int:
        result = 0
        for i in range(len(self.route) - 1):
            result += self.route[i].getDistanceToTown(self.route[i + 1])
        return result

    def getRisque(self) -> float:
        amount = 0
        result = 0
        for i in range(len(self.route) - 1):
            amount += self.route[i].getCashAmount()
            result += amount * self.route[i].getDistanceToTown(self.route[i + 1])
            self.increaseAmount(self.route[i])
        return result
