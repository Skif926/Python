from ClassProduct import Product


def calcul(n, Product):
    count = 0
    for i in range(len(Product)):
        if n / Product[i] == 1:
            count += 1
            Product.pop(i)
    return count


class Order:
    ProductA = Product(3)
    ProductB = Product(6)
    ProductC = Product(6)
    ProductD = Product(6)
    ProductE = Product(1.5)

    def inc(self, Name, long, amount):
        for i in range(amount):
            if Name == 'брус100':
                self.ProductB.addProduct(long)
            elif Name == 'брус50':
                self.ProductA.addProduct(long)
            elif Name == 'доска25':
                self.ProductC.addProduct(long)
            elif Name == 'доска50':
                self.ProductD.addProduct(long)
            elif Name == 'фанера':
                self.ProductE.addProduct(long)

    def counting(self):
        n = self.ProductA.calculation()
        if n != 0:
            print('брус50 3 = ', n)
        n = self.ProductB.calculation()
        if n != 0:
            print('брус100 6 = ', n)
        n = self.ProductC.calculation()
        if n != 0:
            print('доска25 6 = ', n)
        n = self.ProductD.calculation()
        if n != 0:
            print('доска50 6 = ', n)
        n = self.ProductE.calculation()
        if n != 0:
            print('фанера 1,5 = ', n)
