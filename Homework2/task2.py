# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

print('Введите число n ')
n = int(input())

list = []
# result = round((1 + 1/n) ** n, 2)
sum = 0

if n < 1:
    print('Введите число > 0 ')
else:
    n = range(1,n+1)
    for i in n:
        result = round((1 + 1/i) ** i, 2)
        list.append(result)
        sum += result
print(list)
print(sum)