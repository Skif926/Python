from ClassIndustry import industry


class republic:
    Name = ""

    def __init__(self, name):
        self.Name = name
        self.Republicindustry = []
        self.Republicindustry.append(industry("Agriculture"))
        self.Republicindustry.append(industry("LightIndustry"))
        self.Republicindustry.append(industry("GroupA"))
        self.Republicindustry.append(industry("GroupB"))
        self.Republicindustry.append(industry("MilitaryIndustrialComplex"))
        self.Republicindustry.append(industry("Science"))
        self.Republicindustry.append(industry("ChemicalIndustry"))

    def mostbackward(self):
        n = self.Republicindustry[0]
        for i in range(len(self.Republicindustry)):
            if n.getProfitability() > self.Republicindustry[i].getProfitability():
                n = self.Republicindustry[i]
        return n

    def mostbalanced(self):
        n = self.Republicindustry[0]
        for i in range(len(self.Republicindustry)):
            if abs(n.getProfitability()-50) > abs(self.Republicindustry[i].getProfitability() - 50):
                n = self.Republicindustry[i]
        return n

    def mostdeveloped(self):
        n = self.Republicindustry[0]
        for i in range(len(self.Republicindustry)):
            if n.getProfitability() < self.Republicindustry[i].getProfitability():
                n = self.Republicindustry[i]
        return n

    def count(self, a):
        l = []
        if a == 0:
            for i in range(len(self.Republicindustry)):
                if self.Republicindustry[i].getDevelopmentlvl() == "Слабое":
                    l.append(self.Republicindustry[i].getName())
            return l
        elif a == 1:
            for i in range(len(self.Republicindustry)):
                if self.Republicindustry[i].getDevelopmentlvl() == "Сбалансированное":
                    l.append(self.Republicindustry[i].getName())
            return l
        else:
            for i in range(len(self.Republicindustry)):
                if self.Republicindustry[i].getDevelopmentlvl() == "Избыточное":
                    l.append(self.Republicindustry[i].getName())
            return l


