# Реализуйте алгоритм перемешивания списка. НЕ ИСПОЛЬЗОВАТЬ ВСТРОЕННЫЕ БИБЛИОТЕКИ SHUFFLE, 
# максимум использование библиотеки Random для и получения случайного int


print('Введите количество цифр в списке ')
n = int(input())
n_list = list(range(1,n + 1))

print(n_list)

from random import randrange

for i in range(1, n + 1):
    n_1, n_2 = randrange(n), randrange(n)
    n_list[n_1], n_list[n_2] = n_list[n_2], n_list[n_1]

print(n_list)

