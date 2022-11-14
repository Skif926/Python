'''При строительстве важно грамотно рассчитать материалы и их закупить. В этом может
помочь калькулятор материалов. Существует определенный стандарт материалов
который можно заказать
брус 50 3м
брус 100 6м
доска 25 6м
доска 50 6м
фанера 1,5*1,5 м
например заказ такой
3х брус 50 2м
4х брус 50 1,5м
ответ калькулятора
5х брус 50 3м
'''
from Task1.Task_1 import is_digit
from ClassOrder import Order

while True:
    print('Введите заказ в таком формате: Название Длина Количество\n'
          'Список доступных к покупке материалов:\n'
          'брус50 3\n'
          'брус100 6\n'
          'доска25 6\n'
          'доска50 6\n'
          'фанера1,5 1,5\n'
          'Пример заказа: брус50 1,5 x2 доска25 5 6\n'
          'Для выхода введите 0\n')
    Order = Order()
    userinput = input()
    if userinput == '0':
        exit(0)
    userinput = userinput.split()
    count = 0
    dictionary = ['брус50', 'брус100', 'доска25', 'доска50', 'фанера1,5']
    for i in range(len(userinput)):
        if userinput[i] in dictionary:
            count += 1
            i += 1
            if is_digit(userinput[i]) and (float)(userinput[i]) > 0:
                count += 1
                i += 1
            userinput[i] = userinput[i].replace('x', '')
            if is_digit(userinput[i]) and (int)(userinput[i]) > 0:
                count += 1
                if dictionary.index(userinput[i - 2]) == 0:
                    if (float)(userinput[i - 1]) > 3:
                        count -= 1
                        continue
                    Order.incA((float)(userinput[i - 1]), (int)(userinput[i]))

    if count != len(userinput):
        print('Error')
        print('Повторите ввод')
    else:
        break
