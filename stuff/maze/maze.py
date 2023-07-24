import os


board = [
    ['#','#','#','#','#','#','#','#','#','#','#'],
    ['#',' ',' ',' ',' ',' ','#',' ',' ',' ','#'],
    ['#',' ','#','#','#','#','#','#','#',' ','#'],
    ['#',' ',' ',' ','#',' ','#',' ',' ',' ','#'],
    ['#','#','#',' ','#',' ','#',' ','#','#','#'],
    ['#',' ',' ',' ',' ',' ','#',' ',' ',' ','#'],
    ['#','#','#',' ','#','#','#','#','#',' ','#'],
    ['#',' ','#',' ','#',' ',' ',' ',' ',' ','#'],
    ['#',' ','#',' ','#',' ','#',' ','#','#','#'],
    ['#',' ',' ',' ',' ',' ','#',' ',' ',' ','#'],
    ['#','#','#','#','#','#','#','#','#','F','#']
]



player = 'P'
class Maze:

    player_x = 1
    player_y = 1
    running = True


    def print_maze(self):
        os.system('cls')
        board[self.player_y][self.player_x] = player
        print(self.player_y, self.player_x)
        for row in board:
            print(*row, sep="")


    def player_movement(self, player):
        move = input("Move(WASD): ").upper()
        if (move == 'W' and board[self.player_y-1][self.player_x] != '#'):
            board[self.player_y][self.player_x] = ' '
            self.player_y -= 1
        elif (move == 'S' and board[self.player_y+1][self.player_x] != '#'):
            if board[self.player_y+1][self.player_x] == 'F':
                print("Congrats, you beat the maze!")
                self.running = False
            board[self.player_y][self.player_x] = ' '
            self.player_y += 1
        elif (move == 'A' and board[self.player_y][self.player_x-1] != '#'):
            board[self.player_y][self.player_x] = ' '
            self.player_x -= 1
        elif (move == 'D' and board[self.player_y][self.player_x+1] != '#'):
            board[self.player_y][self.player_x] = ' '
            self.player_x += 1




m = Maze()


while m.running:
    m.print_maze()
    m.player_movement(player)