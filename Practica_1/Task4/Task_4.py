'''Задание 4
Для правильной работы нужно соблюдать ритм, чтобы не забывать отдыхать нужен
таймер работы. Напишите таймер в который вводится количество часов минут и
секунд и каждую секунду он выводит сколько осталось времени на таймере.
ПОДСКАЗКА используйте модуль time
'''
import os
from time import sleep
from Practica_1.Task1.Task_1 import is_digit
from ClassTimer import MyTimer


def chose(str):
    if str == 'h' or str == 'h':
        a = 60 * 60
    elif str == 'm' or str == 'M':
        a = 60
    elif str == 's' or str == 'S':
        a = 1
    else:
        return 1
    return a


while True:
    print('Введите время на которое стоит поствить таймер в таком формате:\n'
          'h - час\n'
          'm - минута\n'
          's - секнда\n'
          'Пример: h 24 m 24\n'
          'Для выхода введите 0\n')

    userinput = input()
    if userinput == '0':
        exit(0)
    userinput = userinput.split()
    count = 0
    dictionary = ['h', 'H', 'm', 'M', 's', 'S']
    try:
        for i in range(len(userinput)):
            if userinput[i] in dictionary:
                count += 1
                i += 1
                if is_digit(userinput[i]):
                    count += 1
        if count != len(userinput):
            print('Error')
            print('Повторите ввод')
        else:
            break
    except IndexError:
        print('Error')
        print('Повторите ввод')
timewhait = 0
for i in range(len(userinput)):
    if userinput[i] in dictionary:
        timewhait += chose(userinput[i]) * (int)(userinput[i + 1])

T = MyTimer(timewhait)

while T.timeout():
    T.out()
    T.decTimeout()
    T.correct()
    sleep(1)
    os.system('cls')

print('Alarm таймер завешил работу!')
