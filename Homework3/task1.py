# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позициях с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

print('Введите количество цифр в списке: ')
n = int(input())

from random import randint

if n <= 0:
    print('Введите число > 0')
else:
    list = []
    
    for i in range(n):
        list.append(randint(1,10))
    print('Создадим список из', n, 'рандомных чисел: ')
    print(list)

    list1 = []
    sum = 0

    for i in range(1, len(list), 2):
        list1.append(list[i])
        sum += list[i]
    print('На позициях с нечетным индексом элементы: ', list1)
    print('Сумма этих элементов: ', sum)

    
   

