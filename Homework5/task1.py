#Создайте программу для игры с конфетами человек против человека.
#Условие задачи: На столе лежит заданное количество конфет. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход.
#a) Добавьте игру против бота
#b) Подумайте как наделить бота 'интеллектом'


from random import randint


def input_take(name):
    x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x


def output(name, k, count, value):
    print(f"Ходил {name}, он взял {k}, теперь у него {count}. Осталось на столе {value} конфет.")


player1 = input("Введите имя первого игрока: ")
player2 = input("Введите имя второго игрока: ")
value = int(input("Введите количество конфет на столе: "))
turn = randint(0, 2)  #очередность
if turn:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")

count1 = 0
count2 = 0

while value > 28:
    if turn:
        k = input_take(player1)
        count1 += k
        value -= k
        turn = False
        output(player1, k, count1, value)
    else:
        k = input_take(player2)
        count2 += k
        value -= k
        turn = True
        output(player2, k, count2, value)

if turn:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")