'''Задание 5 Иногда в жизни случаются ошибки. Но нужно уметь с ними работать. Напишите функцию в которой генерируются
случайные цифры (0 и 1). и выполняет деление числа 10 на них. При делении на 0. должно выводится сообщение (“деление на 0”).
 ОСОБЕННОСТЬ. Выполнять данное задание необходимо через конструкцию TRY-EXCEPT'''
import random


def x():
    try:
        return 10 / random.randint(0, 1)
    except ZeroDivisionError:
        print('Деление на 0')




for i in range(10):
    x()