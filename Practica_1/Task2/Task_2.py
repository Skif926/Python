'''Задание 2
Руководителю иногда бывает сложно подобрать слова для речи. Помогите ему создав
генератор случайных фраз из задаваемых слов. Генератор должен работать так: вы
вводите существительные (по одному на строку), после чего идет “стоп слово” и вы
пишете глаголы, также до “стоп слова”. После этого количество фраз которые нужно
сгенерировать. и вывести фразы. с-существительное, г-глагол, типы фраз сгс,гсс,ссг.
(Фразы могут иметь ошибки в склонениях и падежах)'''
import random


def startenter(b):
    str = []
    while True:
        print('Введите', b, 'или чтобы закончить введите \'стоп слово\'')
        a = input()
        if a == 'стоп слово':
            if (b == 'существительное' and len(str)>=2) or (b == 'глагол' and len(str)>=1):
                return str
            else:
                print('Не получится ни одной фразы добавьте слов')
                continue
        if a == '':
            print('Пусто запись не будет добавлена')
            continue

        str.append(a)


def outputA(nounl, verbl, *b):
    if len(b) == 0:
        str = takestr(nounl) + ' ' + takestr(verbl) + ' ' + takestr(nounl)
        return str
    elif len(b) == 1:
        str = takestr(verbl) + ' ' + takestr(nounl) + ' ' + takestr(nounl)
        return str
    elif len(b) == 2:
        str = takestr(nounl) + ' ' + takestr(nounl) + ' ' + takestr(verbl)
        return str


def outputB(nounl, verbl, *b):
    strA = []
    strB = []
    strA += nounl
    strB += verbl
    if len(b) == 0:
        str = takeuniquestr(strA) + ' ' + takeuniquestr(strB) + ' ' + takeuniquestr(strA)
        return str
    elif len(b) == 1:
        str = takeuniquestr(strB) + ' ' + takeuniquestr(strA) + ' ' + takeuniquestr(strA)
        return str
    elif len(b) == 2:
        str = takeuniquestr(strA) + ' ' + takeuniquestr(strA) + ' ' + takeuniquestr(strB)
        return str


def takestr(str):
    if len(str) == 1:
        return str[0]
    return str[random.randint(0, len(str) - 1)]


def takeuniquestr(str):
    if len(str) == 1:
        strout = str[0]
        str.pop(0)
        return strout
    c = len(str) - 1
    a = random.randint(0, c)
    strout = str[a]
    str.pop(a)
    return strout


def generation(nounlocal, verblocal, strprintlocal, countlocal, canlocal):
    brick = 0
    for i in range(countlocal):
        while brick < 1000:
            if brick == 999:
                print('Pilic')
            c = random.randint(0, 2)
            if c == 0:  # сгс
                if canlocal:
                    str = outputA(nounlocal, verblocal)
                else:
                    str = outputB(nounlocal, verblocal)
                if str not in strprintlocal:
                    strprintlocal.append(str)
                    brick = 0
                    break
                else:
                    brick += 1
            elif c == 1:  # гсс
                if canlocal:
                    str = outputA(nounlocal, verblocal, 1)
                else:
                    str = outputB(nounlocal, verblocal, 1)
                if str not in strprintlocal:
                    strprintlocal.append(str)
                    brick = 0
                    break
                else:
                    brick += 1
            else:  # ссг
                if canlocal:
                    str = outputA(nounlocal, verblocal, 1, 2)
                else:
                    str = outputB(nounlocal, verblocal, 1, 2)
                if str not in strprintlocal:
                    strprintlocal.append(str)
                    brick = 0
                    break
                else:
                    brick += 1


random.seed()
noun = startenter('существительное')
verb = startenter('глагол')
count = 0

random.shuffle(noun)
random.shuffle(verb)
countworld = 0
nounworld = 0
userinput = input('Могут существительные повторяться в фразе ? Y\\N\n')
if userinput == 'N' or userinput == 'n' or userinput == '0':
    can = False
    for i in range(len(noun)):
        nounworld += 6 * i
    countworld = nounworld * len(verb)
    print('Максимальное количество уникальных фраз без повтора существительных', countworld)
else:
    can = True
    for i in range(len(noun)):
        nounworld += 6 * i
        countworld = (nounworld + 3 * len(noun)) * len(verb)
    print('Максимальное количество неуникальных фраз с повтором существительных', countworld)
while True:
    try:
        count = int(input('Введите количество фраз которые нужно сгенерировать\n'))
        if count >= 0:
            break
    except ValueError:
        print('Error\n'
              'Некорректный ввод')
        continue
if count > countworld:
    print('Выход за границы возможностей\n'
          'Будет составленно:', countworld, 'фраз')
    count = countworld

strprint = []
generation(noun, verb, strprint, count, can)



if count > len(strprint):
    print('Выход за границы возможностей\n'
          'Будет составленно:', len(strprint), 'фраз')
    count = len(strprint)

strprint.sort()
for i in range(count):
    print(i + 1, ' - ', strprint[i])
