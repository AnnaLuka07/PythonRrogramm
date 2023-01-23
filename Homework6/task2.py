# Задайте число. Составьте список чисел Фибоначчи


#def fib(n):
#    if n in [0,1]:
#        return 1
#    else:
#        return fib(n - 1) + fib(n - 2)
#list = [0]
#n = int(input('Введите число членов последовательности: '))
#for e in range(n):
#    list.append(fib(e))    
#print(list)

def fib(count):
    fib_list = [0, 1]
    any(map(lambda _: fib_list.append(sum(fib_list[-2:])), range(2, count)))
    return fib_list[:count]

n = int(input('Введите число членов последовательности: '))
print(fib(n))

