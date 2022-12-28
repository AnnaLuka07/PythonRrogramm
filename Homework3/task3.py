# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


print('Введите количество вещественных цифр в списке: ')
n = int(input())

from random import uniform

if n <= 0:
    print('Введите число > 0')
else:
    list = []                              # Создадим список из n рандомных чисел:
    for i in range(n):
        list.append(round(uniform(1, n), 2))
    print(list)

    max = min = list[0] % 1
    result = 0
    i = 1
    for i in range(len(list)):
        num = round(list[i] % 1, 2)
        if num > max:
            max = num
        if num < min:
            min = num
    result = round((max - min), 2)
    print('Разница между мах и мин значением дробной части элементов списка = ', result)


