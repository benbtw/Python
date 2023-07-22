import os

@staticmethod
def print_board():
    count = 0
    board = ['|', '  ', '|', '  ', '|', '  ', '|',
         '|','--','|','--','|','--','|',
         '|', '  ', '|', '  ', '|', '  ', '|',
         '|','--','|','--','|','--','|',
         '|', '  ', '|', '  ', '|', '  ', '|']
    for i in board:
        if i == '|':
            count += 1
        if count == 4 or count == 8 or count == 12 or count == 16:
            print(i,end='\n')
        else:
            print(i, end='')

@staticmethod
def play_game():
    computer = ''
    player = input('Would you like to be X or O: ').upper()
    while True:
        os.system('cls')
        if player == "X" or player == "O":
            break
        else:
            print('Error, enter X or O', end='\n')
            player = input('Would you like to be X or O: ').upper()

    if player == 'X':
        computer = 'O'
    elif player == 'O':
        computer = 'X'

    print(f'You have chosen {player}, good luck.')
                          

os.system('cls')
play_game()