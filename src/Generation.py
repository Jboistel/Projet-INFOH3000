import Solution


class Generation:
    solutions: [Solution]

    def __init__(self, solutions: [Solution]):
        self.solutions = solutions


"""
    def reproduce(self):
        newSolutions = []
        for i, solution in enumerate(self.solutions):

    def mutate(self):

    def selection(self):
        self.solutions.sort(key=lambda s: s.calculateScore())
        self.solutions = self.solutions[:len(self.solutions)/2]
"""