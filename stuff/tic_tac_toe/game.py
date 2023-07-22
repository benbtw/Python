import os, math, random, time

board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
open_spots = [1,2,3,4,5,6,7,8,9]
winner = None
gameRunning = True

def print_board():
    print('|'+ board[0] + '|' + board[1] + '|' + board[2] + '|')
    print('-------')
    print('|'+ board[3] + '|' + board[4] + '|' + board[5] + '|')
    print('-------')
    print('|'+ board[6] + '|' + board[7] + '|' + board[8] + '|')

def move(player, computer):
    player_move = 0
    player_spot = ''
    computer_move = 0
    ok_spot = True

    while ok_spot:
        player_spot = int(input('Which spot would you like to choose(1-9): '))
        player_move = int(player_spot) - 1
        if player_spot > 0 and  player_spot < 10 and board[player_move] == ' ':
            player_move = int(player_spot) - 1
            open_spots.remove(int(player_spot))
            board[player_move] = player
            ok_spot = False
        else:
            print('Error')
        
        if open_spots == []:
            break
        computer_move = random.choice(open_spots)
        open_spots.remove(computer_move)
        board[computer_move-1] = computer

            
    time.sleep(0.3)

def checkHorizontle():
    global winner
    if board[0] == board[1] == board[2] and board[0] != " ":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != " ":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != " ":
        winner = board[6]
        return True
    
def checkRow():
    global winner
    if board[0] == board[3] == board[6] and board[0] != " ":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != " ":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != " ":
        winner = board[3]
        return True
    
def checkDiag():
    global winner
    if board[0] == board[4] == board[8] and board[0] != " ":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != " ":
        winner = board[2]
        return True
    
def checkIfWin():
    global gameRunning
    if checkHorizontle():
        print_board()
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkRow():
        print_board()
        print(f"The winner is {winner}!")
        gameRunning = False

    elif checkDiag():
        print_board()
        print(f"The winner is {winner}!")
        gameRunning = False


def checkIfTie():
    global gameRunning
    if " " not in board:
        print_board(board)
        print("It is a tie!")
        gameRunning = False
    

player = 'X'
computer = 'O'


while gameRunning:
    os.system('cls')
    print_board()
    move(player, computer)
    checkIfWin()
    checkIfTie()