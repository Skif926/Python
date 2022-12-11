'''
Отлично, фразы получаются, но иногда руководитель пишет и свои речи и допускает
ошибки. Нужно чтобы программа проверяла правильно ли написаны слова. Вводятся
“правильные” слова которыми будет проверятся, после чего вводится предложение
слова из которого проверяются. после выводятся слова с ошибками(ошибка
отделяется пробелом справа и слева от буквы). ПОДСКАЗКА нужно проверять на
минимальное отличие от “эталонного” слова.
'''


def check(dictionarylocal, inputstr):
    a = []
    outputstr = []
    for jj in range(len(dictionarylocal)):
        a.append(0)
        outputstr.append('')

    for j in range(len(dictionarylocal)):
        if len(inputstr) - len(dictionarylocal[j]) <= -1:
            a[j] = 10

    for k in range(len(inputstr)):
        for j in range(len(dictionarylocal)):
            if a[j] < 2:

                if inputstr[k] == dictionarylocal[j][k]:
                    a[j] -= 1
                    outputstr[j] += inputstr[k]
                    # print('a[',j,'] =',a[j], ' i = ', k, 'j = ', j, 'str = ', outputstr[j])
                else:
                    a[j] += 1
                    outputstr[j] += '_' + dictionarylocal[j][k].upper() + '_'
                    # print('a[',j,'] =',a[j], 'i = ', k, 'j = ', j, 'str = ', outputstr[j])


    val, idx = min((val, idx) for (idx, val) in enumerate(a))
    # print('Min = ', val,
    #      '\nIndx = ', idx)

    if val != 2:
        return outputstr[idx]
    else:
        return inputstr


dictionary = ['собака', 'кошка', 'хомяк']
userinput = 'коiка собака сабака летучая мышь и хамяк Пользоватеьский'
print('Пользоватеьский ввод:', userinput)
treatmentinput = []
treatmentinput = userinput.split()
for i in range(len(treatmentinput)):
    if treatmentinput[i] not in dictionary:
        treatmentinput[i] = check(dictionary, treatmentinput[i])
print('Обработанный вывод:', " ".join(treatmentinput))
