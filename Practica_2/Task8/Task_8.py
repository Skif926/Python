'''Задание 8 Продолжая работать с файлами важно не захламлять пространство и не терять что то важное.
Напишите функцию которая создает копию файла, но при этом удаляет оригинал. '''
import os
import shutil


def x():
    if os.path.isfile('text.txt'):
        shutil.copy('text.txt', 'textcopy.txt')
        os.remove('text.txt')

f = open('text.txt', 'w')
f.close()
x()
