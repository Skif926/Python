"""для более удобного обзора при перераспределении ресурсов важно знать откуда и
куда их нужно перенаправить. Создайте инструмент для удобного доступа к такой
статистике.
Существуют определенные отрасли:
Сельское хозяйство
Легкая промышленность
Тяжелая промышленность группы А
Тяжелая промышленность группы Б
Военно промышленный комплекс
Наука
Химическая промышленность
Вы вводите количество “союзных республик” и даете им названия (можете просто
случайно присваивать им названия из какого то списка внутри программы)
и случайно присваиваете им все отрасли в разделы
избыточно развитые
сбалансированно развитые
слабо развитые
после чего ваш “инструмент” должен вывести статистику
1. Самая отстающая отрасль в союзных республиках (наиболее часто встречающая
слабо развитая отрасль у всех) и насколько она отстающая
2. Самая развитая отрасль ( наиболее часто встречающая избыточно развитая
отрасль у всех) и насколько она развитая
3. Самая сбалансированная отрасль ( тоже самое только с сбалансированным
развитием) и насколько она сбалансированная
4. статистика отраслей отраслей (сумма между избыточно развитыми и
слаборазвитыми в одно отрасли по всем республикам)
"""
import random

from ClassRepublic import republic

k = random.randint(1, 1000)
replist = []
backward = []
profit = []
balanced = []
Agriculture = 0
LightIndustry = 0
GroupA = 0
GroupB = 0
MilitaryIndustrialComplex = 0
Science = 0
ChemicalIndustry = 0

for i in range(k):
    n = republic(i)
    backward += n.count(0)
    profit += n.count(2)
    balanced += n.count(1)
    Agriculture += n.Republicindustry[0].getProfitability()
    LightIndustry += n.Republicindustry[1].getProfitability()
    GroupA += n.Republicindustry[2].getProfitability()
    GroupB += n.Republicindustry[3].getProfitability()
    MilitaryIndustrialComplex += n.Republicindustry[4].getProfitability()
    Science += n.Republicindustry[5].getProfitability()
    ChemicalIndustry += n.Republicindustry[6].getProfitability()
    replist.append(n)
print("Самая отстающая отрасль", max(backward, key=backward.count))
print("Самая развитая отрасль", max(profit, key=profit.count))
print("Самая сбалансированная отрасль", max(balanced, key=balanced.count))
print("Среднее развитие отраслей:\n"
      f"Agriculture: {Agriculture/k:.2f}\t"
      f"LightIndustry: {LightIndustry/k:.2f}\t"
      f"GroupA: {GroupA/k:.2f}\t"
      f"GroupB: {GroupB/k:.2f}\t"
      f"MilitaryIndustrialComplex: {MilitaryIndustrialComplex/k:.2f}\t"
      f"Science: {Science/k:.2f}\t"
      f"ChemicalIndustry: {ChemicalIndustry/k:.2f}\t")

