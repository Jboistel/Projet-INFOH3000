class Truck:
    def __init__(self, route = []):
        self.route = route

    def getAmount(self):
        amount = 0
        for town in self.route:
            amount += town.getCashAmount()
        return amount

    def getRoute(self):
        return self.route