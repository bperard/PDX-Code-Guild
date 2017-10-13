'''
lab 23 - blackjack advice
'''

import random
import Blackjack

# initiate card selection(element)/value(index) list, hand/score/ace tracker variables
cards = [11, 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
hand = []
score = 0
aced = 0

# Intro and mode selection
print('Ready to test your luck in a game of Blackjack?... OF COURSE YOU ARE!\n'
      'Quick refresher: Your goal is to get your cards to total 21, without going over.\n'
      'Face cards are worth 10, an Ace can be worth one or eleven. Possible cards are:\n'
      'A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K.')
mode = input('Would you like to "choose" cards, or be "dealt"?:')



# player chosen cards mode
if mode.lower() == 'choose':
    # card choice
    hand.append(input('Choose your first card:').upper())
    hand.append(input('Choose your second card:').upper())
    hand.append(input('Choose your third card:').upper())

    # tally score in hand
    for value in hand:
        if value in cards:
            score += cards.index(value)    # index used as card value
            if cards.index(value) > 10:
                score -= cards.index(value) % 10    # correct face card values
            if value == 'A':
                aced += 1    # ace counter
        else:
            print(value + ' is not a playable card, you had one job...')    # failed choice
            score += 20    # punish player

    # check score values for aces held, keep highest without bust
    held = 0
    while held < aced:
        score += 10
        if score > 21:
            score -= 10
        held += 1

    # advise player based on current score
    if 0 < score < 17:
        print(hand)
        print(str(score) + ' Hit')
    elif 17 <= score < 21:
        print(hand)
        print(str(score) + ' Stay')
    elif score == 21:
        print(hand)
        print(str(score) + ' Blackjack!')
    elif score > 21:
        print(hand)
        print(str(score) + ' Already Busted')

# unsupported player mode
elif mode.lower() != 'dealt' and mode.lower() != 'choose':
    print('In order use the ' + mode + ', you have to first purchase the "Pirates vs. Ninjas" DLC.')

# start game of Blackjack
elif mode.lower() == 'dealt':
    hand = Blackjack.deal_card()
    hand = Blackjack.deal_card()
    print(hand)
    # will return to finish this mode




