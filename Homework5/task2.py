#Создайте программу для игры в 'Крестики-нолики'

print('*'*100)
print('\n')
print('Давайте сыграем в крестики нолики?')

field = list(range(1,10))

def design_field(field):
    print('-'*12)
    for i in range(3):
        print('|', field[0+i*3],'|', field[1+i*3], '|', field[2+i*3], '|')
        print('-'*12)


def choice(move):
    valid = False
    while not valid:
        player_index = input('Ваш ход, выберите ячейку ' + move + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Что то не то нажали')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(field[player_index-1]) not in 'XO'):
                field[player_index-1] = move
                valid = True
            else:
                print('Занято')
        else:
            print('Попробуйте еще раз')

def victory_check(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]
    return False

def game(field):
    counter =0
    vic = False
    while not vic:
        design_field(field)
        if counter % 2 == 0:
            choice('X')
        else:
            choice('0')
        counter +=1
        if counter > 4:
            tt_win = victory_check(field)
            if tt_win:
                print(tt_win,'Победа')
                vic = True
                break
            if counter == 9:
                print('Ничья!)')
        design_field(field)
game(field)