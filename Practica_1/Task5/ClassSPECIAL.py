import random


class SPECIAL:
    Strength = 1
    Perception = 1
    Endurance = 1
    Charisma = 1
    Intelligence = 1
    Agility = 1
    Luck = 1
    Freepoints = 21

    @staticmethod
    def randomSet():
        random.seed()
        while SPECIAL.Freepoints > 0:
            r = random.randint(1, 9)
            c = random.randint(1, 7)
            if SPECIAL.Freepoints < r:
                r = SPECIAL.Freepoints
            if c == 1:
                if SPECIAL.Strength + r <= 10:
                    SPECIAL.Strength += r
                    SPECIAL.Freepoints -= r
            elif c == 2:
                if SPECIAL.Perception + r <= 10:
                    SPECIAL.Perception += r
                    SPECIAL.Freepoints -= r
            elif c == 3:
                if SPECIAL.Endurance + r <= 10:
                    SPECIAL.Endurance += r
                    SPECIAL.Freepoints -= r
            elif c == 4:
                if SPECIAL.Charisma + r <= 10:
                    SPECIAL.Charisma += r
                    SPECIAL.Freepoints -= r
            elif c == 5:
                if SPECIAL.Intelligence + r <= 10:
                    SPECIAL.Intelligence += r
                    SPECIAL.Freepoints -= r
            elif c == 6:
                if SPECIAL.Agility + r <= 10:
                    SPECIAL.Agility += r
                    SPECIAL.Freepoints -= r
            elif c == 7:
                if SPECIAL.Luck + r <= 10:
                    SPECIAL.Luck += r
                    SPECIAL.Freepoints -= r

    def setStrength(self, x):
        self.Strength = x

    @staticmethod
    def getStrength():
        return SPECIAL.Strength

    def setPerception(self, x):
        self.Perception = x

    @staticmethod
    def getPerception():
        return SPECIAL.Perception

    def setEndurance(self, x):
        self.Endurance = x

    @staticmethod
    def getEndurance():
        return SPECIAL.Endurance

    def setCharisma(self, x):
        self.Charisma = x

    @staticmethod
    def getCharisma():
        return SPECIAL.Charisma

    def setIntelligence(self, x):
        self.Intelligence = x

    @staticmethod
    def getIntelligence():
        return SPECIAL.Intelligence

    def setAgility(self, x):
        self.Agility = x

    @staticmethod
    def getAgility():
        return SPECIAL.Agility

    def setLuck(self, x):
        self.Luck = x

    @staticmethod
    def getLuck():
        return SPECIAL.Luck

    def decFreepoints(self, x):
        self.Freepoints -= x
