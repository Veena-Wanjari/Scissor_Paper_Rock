#import modules
from random import randint

#declare variables
player = input("rock(r), paper(p), scissors(s)")
chosen = randint(1,3)

#print(player vs challenger)
print(player, 'vs', end = " ")

#print chosen

if chosen == 1:
    computer = 'r'
elif chosen == 2:
    computer = 'p'
elif chosen == 3:
    computer = 's'
    
print(computer)

if player == computer:
    print("DRAW!")

elif player == 'r' and computer =='s':
    print('Player Wins! : Rock beats Scissors')

elif player == 'r' and computer == 'p':
    print('Computer wins! : Paper covers Rock')

elif computer == 'p' and player == 's':
    print('Player Wins!: Scissors cut Paper')

elif player == 's' and computer == 'r':
    print('Computer wins! : Rock beats Scissors')

elif player == 'p' and computer == 'r':
    print('Player Wins: Paper covers Rock')