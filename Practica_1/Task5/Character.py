import random

from ClassSPECIAL import SPECIAL


class Character:
    Names = ["Адам Тэйлор", "Карен Бишоп", "Хосе Дин", "Джемма Фултон", "Джошуа Грин", "Кимберли Эванз"]
    Name = ''
    Age = 0
    Classes = ["Боец", "Дикарь", "Проныра", "Лидер", "Везунчик", "Умник"]
    Class = ''
    Special = SPECIAL
    Skillses = ["Взлом", "Лёгкое оружие", "Тяжёлое оружие", "Без оружия", "Азартные игры", "Наука"]
    Skills = []

    def __init__(self):
        self.Special.randomSet()
        self.Name = random.choice(self.Names)
        self.Age = random.randint(10, 80)
        self.Class = random.choice(self.Classes)
        self.Skills.append(random.sample(self.Skillses, random.randint(1, 6)))

    def __str__(self):
        return f"Имя: {self.Name}, Возраст: {self.Age}, Класс: {self.Class}, Навыки: {self.Skills}\n" \
               f"Сила {self.Special.getStrength()}\n" \
               f"Восприятие {self.Special.getPerception()}\n" \
               f"Выносливость {self.Special.getEndurance()}\n" \
               f"Харизма {self.Special.getCharisma()}\n" \
               f"Интеллект {self.Special.getIntelligence()}\n" \
               f"Ловкость {self.Special.getAgility()}\n" \
               f"Удача {self.Special.getLuck()}"
