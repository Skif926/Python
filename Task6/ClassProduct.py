class Product:
    def __init__(self, maxlong):
        self.oderlist = []
        self.maxlong = (float)(maxlong)
        self.buyamount = 0

    def addProduct(self, long):
        self.oderlist.append(long)

    def calculation(self):
        if len(self.oderlist) == 0:
            return
        remainder = 0.0
        self.oderlist.sort()
        self.oderlist.reverse()
        while True:
            if len(self.oderlist) > 0:
                if self.maxlong % self.oderlist[0] != 0:
                    remainder = self.maxlong % self.oderlist[0]
                    self.oderlist.pop(0)
                    self.buyamount += 1
                else:
                    remainder = self.maxlong - self.oderlist[0]
                    self.oderlist.pop(0)
                    self.buyamount += 1
                self.calculationhelp(remainder)
            else:
                return self.buyamount


    def calculationhelp(self, remainder):
        if len(self.oderlist) > 0:
            for i in range(len(self.oderlist)):
                if remainder - self.oderlist[i] >= 0:
                    remainder -= self.oderlist[i]
                    self.oderlist.pop(i)
                    self.calculationhelp(remainder)
                    break

