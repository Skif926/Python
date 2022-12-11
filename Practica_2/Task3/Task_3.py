'''Задание 3 Нам необходимо понять нет ли у нас неповторяющихся в производстве на разных заводах товаров.
Напишите программу которая создает 2 множества, заполняет их случайным количеством “товаров” (рыба,мясо,сталь,игрушки и т.д
из заранее сформированного вами списка (не меньше 15 “товаров”) а после сравнивает их и на выход поступают те что не повторяются на обоих. .
'''

import random


dictionary = ['рыба', 'мясо', 'сталь', 'игрушки', 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
setsA = set(random.sample(dictionary, random.randint(1, 5), counts=None))
setsB = set(random.sample(dictionary, random.randint(1, 5), counts=None))
dictionary = set(dictionary)
dictionary = dictionary.difference(setsA)
dictionary = dictionary.difference(setsB)
print(dictionary)
