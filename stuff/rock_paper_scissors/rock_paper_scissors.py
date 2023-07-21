import random

def play():
    user = input("rock, paper, or scissors: ").lower()
    computer = random.choice(['rock', 'paper', 'scissors'])
    
    if user == computer:
        print(f'You picked {user} and computer picked {computer}')
        return 'tie'
    
    if is_win(user, computer):
        return f'You won with {user} and computer lost with {computer}'
    return f'You lost with {user} and computer won with {computer}'

def is_win(player, opponent):
    if (player == 'rock' and opponent == 'scissors') \
    or (player == 'scissors' and opponent == 'paper') \
    or (player == 'paper' and opponent == 'rock'):
        return True
    
print(play())