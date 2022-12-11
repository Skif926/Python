import random


class industry:
    name = "undefined"
    profitability = 0
    developmentlvl = "undefined"

    def __init__(self, name):
        self.name = name
        self.initialization()
        self.determinedev()

    def initialization(self):
        self.profitability = random.randint(0, 100)

    def determinedev(self):
        if self.profitability <= 33:
            self.developmentlvl = "Слабое"
        elif self.profitability <= 66:
            self.developmentlvl = "Сбалансированное"
        else:
            self.developmentlvl = "Избыточное"

    def getProfitability(self):
        return self.profitability

    def getName(self):
        return self.name

    def getDevelopmentlvl(self):
        return self.developmentlvl
