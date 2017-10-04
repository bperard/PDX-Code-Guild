'''
Rock, paper, scissors against the computer
'''

import random

throws = ['rock', 'paper', 'scissors'] #comp choices
comp = random.choice(throws)

player = input('Think you can beat me in a game of Roshambo? I doubt it, but let\'s give it a shot.\n Choose your weapon: paper, rock, scissor.').lower() #player prompt

while player == comp: #check for tie, and replay
    player = input('It\'s a tie, we can\'t end without a loser. Type "done," or throw again.').lower()
    comp = random.choice(throws)
    if player == 'done':
        break

# rock outcome
if player == 'rock':
    if comp == 'scissors':
        print('You must be very proud of yourself, you win.')
    else:
        print('Computers are the future, this is just the beginning; you lose.')
# scissors outcome
elif player == 'scissors':
    if comp == 'paper':
        print('You must be very proud of yourself, you win.')
    else:
        print('Computers are the future, this is just the beginning; you lose.')
# paper outcome
elif player == 'paper':
    if comp == 'rock':
        print('You must be very proud of yourself, you win.')
    else:
        print('Computers are the future, this is just the beginning; you lose.')
# horrible person outcome
else:
    print('There were three choices... how did you mess that up; you lose.')