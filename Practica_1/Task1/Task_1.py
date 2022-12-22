'''
Задание 1
Для повышения эффективности работы инженера ему нужно быстрее считать. В этом
ему поможет калькулятор. напишите калькулятор с функциями (+,-,*,/) а так же
возведение в степень, остаток от деления, извлечение корня. В случае невозможных
вычислений он должен выдавать “Error”.
'''

import os
import time
from cmath import inf


clear = lambda: os.system('cls')
addition = lambda x, y: x + y
subtraction = lambda x, y: x - y
multiplication = lambda x, y: x * y
division = lambda x, y: x / y
exponentiation = lambda x, y: x ** y
remainderdivision = lambda x, y: x % y
rootextraction = lambda x: x ** (1 / 2)


def userinput(*b):
    while True:
        print('Введите число')
        a = input()
        if is_digit(a) and not b:
            if float(a) == inf:
                print('Это число для меня слишком большое, я ведь только начинающий калькулятор')
                continue
            return a
        elif is_digit(a) and len(b) == 1 and float(a) != 0:
            return a
        elif a.isdigit() and len(b) == 2:
            return a
        elif is_digit(a) and a.isdigit() == False and len(b) == 2 and float(a) < 0:
            print('Это число отрицательное, в результате будет использовано положительное число')
            return float(a) * (-1)
        elif is_digit(a) and a.isdigit() == False and len(b) == 2 and float(a) >= 0:
            return float(a)
        else:
            print('Error\n'
                  'Некорректный ввод')


def is_digit(a):
    try:
        float(a)
        return True
    except ValueError:
        return False


def continuecounting():
    print('Продолжить вычисления? (1,Y)')
    a = input()
    return a in ['1', 'y', 'Y']


def calcul():
    print('Привет я калькулятор!\n'
          'Каждому инженеру нужен калькулятор для повышения эффективности рабоы\n'
          'Какую операцию выполнить:\n'
          '1 - Сложение\n'
          '2 - Вычитание\n'
          '3 - Умножение\n'
          '4 - Деление\n'
          '5 - Возведение в степень\n'
          '6 - Остаток от деления\n'
          '7 - Извлечение корня\n'
          '0 - Выход')
    strInput = input()
    if strInput.isdigit() and int(strInput) in range(8):
        if int(strInput) == 1:
            clear()
            print('Операция Cложение A + B ')
            a = addition(float(userinput()), float(userinput()))
            if a == inf:
                print('Error\n'
                      'Полученное число для меня слишком большое, я ведь только начинающий калькулятор')
            print('Ответ: ', a)
            return continuecounting()
        elif int(strInput) == 2:
            clear()
            print('Операция Вычитание A - B ')
            a = subtraction(float(userinput()), float(userinput()))
            if a == inf:
                print('Error\n'
                      'Полученное число для меня слишком большое, я ведь только начинающий калькулятор')
            print('Ответ: ', a)
            return continuecounting()
        elif int(strInput) == 3:
            clear()
            print('Операция Умножение A * B ')
            a = multiplication(float(userinput()), float(userinput()))
            if float(a) == inf:
                print('Error\n'
                      'Полученное число для меня слишком большое, я ведь только начинающий калькулятор')
            print('Ответ: ', a)
            return continuecounting()
        elif int(strInput) == 4:
            clear()
            print('Операция Деление A \\ B ')
            a = division(float(userinput()), float(userinput(True)))
            if a == inf:
                print('Error\n'
                      'Полученное число для меня слишком большое, я ведь только начинающий калькулятор')
            print('Ответ: ', a)
            return continuecounting()
        elif int(strInput) == 5:
            clear()
            print('Операция Возведение в степень A ^ B ')
            a = exponentiation(float(userinput()), float(userinput()))
            if a == inf:
                print('Полученное число для меня слишком большое, я ведь только начинающий калькулятор')
            print('Ответ: ', a)
            return continuecounting()
        elif int(strInput) == 6:
            clear()
            print('Операция Остаток от деления A mod B ')
            print('Ответ: ', remainderdivision(float(userinput(0, 0)), float(userinput(0, 0))))
            return continuecounting()
        elif int(strInput) == 7:
            clear()
            print('Операция Извлечение корня √A')
            print('Ответ: ', rootextraction(float(userinput(0, 0))))
            return continuecounting()
        elif int(strInput) == 0:
            return False

    else:
        print('Error\n'
              'Некорректный выбор операции')

    return True


if __name__ == '__main__':
    while calcul():
        time.sleep(1)
        clear()
        continue