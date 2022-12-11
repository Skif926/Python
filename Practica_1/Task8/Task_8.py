"""Задание 8*
игра в планирование
существую определенные отрасли в вашей республике:
Сельское хозяйство
Тяжелая промышленность
Легкая промышленность
Военно промышленный комплекс.
суть игры в том, что Каждая из отраслей потребляет или создает другую отрасль
(кроме Тяжпрома она и создает и потрябляет).
СХ - ничего не потребляет но создает Тяж Пром
Тяж Пром создает СХ ЛП и ВПК, но потребляет СХ
ЛП потребляет Тяж Пром, но какая то часть потребляется населением каждый ход
ВПК потребляет Тяж Пром, но какая то часть потребляется внешней борьбой каждый
ход
у игры есть 3 вида окончания
1. ЛП ушла в “минус” - потребительский кризис вы проиграли
2. ВПК ушел в “минус” - вас захватили вы проиграли
3. ВПК выше какого то порога - вы победили и захватили всех.
Ваша задача как игрока перераспределять отрасли друг в друга каждый ход (не
забывая что каждый ход они потребляют и производят что то ).
Как разработчику вам нужно создать вычисления перераспределения и
“сбалансировать” коэффициенты производства"""

pop = 100
agr = 1200
heavy = 0
ligh = 0
VPK = 0
fight = 0
popl = pop
popfree = 0


class Game:
    def __init__(self):
        self.pop = 100
        self.agr = 1200
        self.heavy = 0
        self.ligh = 0
        self.VPK = 0
        self.fight = 0
        self.fight = 0

    def start(self):
        while True:
            self.VPK = 0
            self.setfight()
            self.setheavy()
            while True:
                x = input(f'Выделите % тяжелой промышленности({self.heavy:.2f}) для Сельского хозяйства :')
                if 100 >= int(x) >= 0:
                    break
            self.setagr(int(x) / 100 * self.heavy)
            self.heavy -= int(x) / 100 * self.heavy
            while True:
                x = input(
                    f'Выделите % тяжелой промышленности({self.heavy:.2f}) для Легкой промышленности(Осталось:{self.ligh:.2f}/Нужно:{self.pop * 3:.2f}) :')
                if 100 >= int(x) >= 0:
                    break
            self.setlight(int(x) / 100 * self.heavy)
            self.heavy -= int(x) / 100 * self.heavy
            while True:
                x = input(
                    f'Выделите % тяжелой промышленности({self.heavy:.2f}) для Военно промышленный комплекса(Нужно:{self.fight:.2f}) :')
                if 100 >= int(x) >= 0:
                    break
            self.setVKK(int(x) / 100 * self.heavy)
            self.decVKK()
            self.heavy -= int(x) / 100 * self.heavy
            self.declight()
            print(f'Население потратило легкую промышленность {self.pop * 3:.2f} осталось {self.ligh:.2f}')
            self.setpop()
            if self.ligh < 0:
                print('Вы проиграли населению нечего есть')
                break
            if self.VPK < 0:
                print('Вы проиграли войну')
                break
            if self.VPK - 1000 > self.fight * 100:
                print('Вы выиграли !')
                break

    def setagr(self, x):
        self.agr = x * self.pop / 10

    def setheavy(self):
        self.heavy += self.agr * 0.1 * (1 + self.pop * 0.1)

    def setlight(self, x):
        self.ligh += x

    def declight(self):
        self.ligh -= self.pop * 3

    def setVKK(self, x):
        self.VPK = x

    def decVKK(self):
        self.VPK -= self.fight

    def setpop(self):
        if 0 < self.ligh <= self.pop * 3 * 1.5:
            self.pop = int(self.pop * 1.1)
            print(f'Население почти не изменилось: {self.pop}')
        elif self.pop * 3 * 1.5 < self.ligh <= self.pop * 3 * 3:
            self.pop = int(self.pop * 1.5)
            print(f'Население изменилось: {self.pop}')
        elif self.pop * 3 * 3 < self.ligh <= self.pop * 3 * 4:
            self.pop = int(self.pop * 2.5)
            print(f'Население сильно изменилось: {self.pop}')
        elif self.ligh > self.pop * 3 * 4:
            self.pop = int(self.pop * 3 + self.ligh * 0.001)
            print(f'Население очень сильно изменилось: {self.pop}')

    def setfight(self):
        self.fight = self.fight * 1.3 + self.ligh * 0.2 + self.agr * 0.5 + self.pop * 4 - 1000


A = Game()
A.start()
