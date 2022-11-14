def calcul(n, Product):
    count = 0
    for i in range(len(Product)):
        if n / Product[i] == 1:
            count += 1
            Product.pop(i)
    return count


class Order:
    ProductA = []
    ProductB = []
    ProductC = []
    ProductD = []
    ProductE = []

    def incA(y, x):
        for i in range(x):
            Order.ProductA.append(y)

    def calculation(self):
        if len(self.ProductA) == 0:
            return
        n = 6
        count = 0
        remainder = 0
        self.ProductA.sort()
        self.ProductA.reverse()
        count += calcul(n, self.ProductA)
        while True:
            if remainder == 0 and len(self.ProductA) > 0:
                remainder = n % self.ProductA[0]
                count += 1
                self.ProductA.pop(0)
            if len(self.ProductA) > 0:
                for i in range(len(self.ProductA)):
                    if remainder - self.ProductA[i] >= 0:
                        remainder -= self.ProductA[i]
                        self.ProductA.pop(i)
                        break
                    if i == len(self.ProductA):
                        remainder = 0
            else:
                print(count)
                break


c = Order
c.incA(4, 2)
c.incA(1, 1)
c.incA(5, 1)
c.incA(2, 1)
c.calculation(Order)
