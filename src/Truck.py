class Truck:
    route: [str]
    amount: int

    def __init__(self, route=[]):
        self.route = route

    def getAmount(self):
        self.amount = 0
        for town in self.route:
            self.amount += town.getCashAmount()
        return self.amount

    def getRoute(self):
        return self.route
