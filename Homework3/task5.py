# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

#k = int(input('Введите число'))

def fib(n):
    if n in [0,1]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
list = [0]
n = int(input('Введите число членов последовательности: '))
for e in range(n):
    list.append(fib(e))
    #list.insert(?????)         не доходит до меня, что надо сделать, чтобы было правильно слева от 0...все перепробовала...      
print(list)
