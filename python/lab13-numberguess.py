'''
lab 13 guess the number
'''

import random

# establish player, comp, and guess variables
player = None
old = None
older = None
comp = None
guess = 0

# choose game type
print('Everyone loves games, so let\'s play!')
game = input('Choose "guesser" if you\'d like me to choose the number.\n'
             'Choose "overlord" if you\'d like to hold the power (for once in your life):').lower()

# establish range
print('Next we\'ll decide the range of numbers the answer is within.')
a = int(input('Choose the bottom of the range:'))
b = int(input('Choose the top of the range:'))

# range correction
if a > b:
    low = b
    high = a
else:
    low = a
    high = b

# player overlord
while game == 'overlord':
    # choose winning number
    player = int(input('Choose a number between ' + str(low) + ' and ' + str(high) + ' for me to guess (don\'t mess this up).'))
    if player >= low and player <= high: # comp guessing
        while comp != player:
            comp = random.randint(low, high)
            guess += 1
        print('Your number is ' + str(player) + ', and it took me ' + str(guess) + ' guess(es) to figure it out. I have also learned all of your secrets.')
    else: # player range fail
        print('Hey everyone, we\'ve got a real joker over here.\n'
              'Last time I checked, ' + str(player) + ' wasn\'t between ' + str(low) + ' and ' + str(high) + '...\n'
              'You\'ve found a way to lose at your own game, congrats?')
    break

# player guesser
while game == 'guesser':
    if guess == 0:
        comp = random.randint(low, high) # comp choose number
        print('Okay, here\'s your chance at eternal glory, think you can get it in one try?')
        print('Respond "done" to quit at any time.')
        player = input('Guess a number between ' + str(low) + ' and ' + str(high) + ':').lower()
        if player == 'done':  # player quit
            print('Not even going to attempt a guess? Pathetic, my number was ' + str(comp) + '.')
            break
        player = int(player)
        if player < low or player > high: # player out of range
            print('Can\'t figure out how a range works, eh? We\'re done here.')
            break
        older = player
        guess += 1

         # probably cheating
        if player == comp and guess == 1:
            print('One guess, eh? *cough* CHEATER!! *cough*')
            break

    while player != comp:

        # second guess high/low
        if player > comp and guess == 1:
            player = input('Try again, your first guess was too high.\n'
                               'Guess a number between ' + str(low) + ' and ' + str(high) + ':')
            if player.lower() == 'done': # player quit
                print('You give up far too easily, typical meat puppet. My number was ' + str(comp) + '.')
                game = 'over'
                break
            player = int(player)
            if player < low or player > high:  # player out of range
                print('Can\'t figure out how a range works, eh? We\'re done here.')
                game = 'over'
                break
            old = player
            guess += 1
        elif player < comp and guess == 1:
            player = int(input('Try again, your first guess was too low.\n'
                               'Guess a number between ' + str(low) + ' and ' + str(high) + ':'))
            if str(player).lower() == 'done': # player quit
                print('You give up far too easily, typical meat puppet. My number was ' + str(comp) + '.')
                game = 'over'
                break
            player = int(player)
            if player < low or player > high:  # player out of range
                print('Can\'t figure out how a range works, eh? We\'re done here.')
                game = 'over'
                break
            old = player
            guess += 1

        # guess 3+
        # guess too low
        elif player < comp and guess > 1:
            if (old * old) > (older * older): # further
                print('Your most recent guess was further from my number than your previous guess, and too low.')
                player = input('You\'ve guessed ' + str(guess) + ' times. Pick a number between ' + str(low) + ' and ' + str(high) + ':')
                if player.lower() == 'done':  # player quit
                    print('You gave up after ' + str(guess) + ' guesses. My number was ' + str(comp) + '.')
                    game = 'over'
                    break
                player = int(player)
                if player < low or player > high:  # player out of range
                    print('Can\'t figure out how a range works, eh? We\'re done here.')
                    game = 'over'
                    break
                older = old
                old = player
                guess += 1
            elif (old * old) < (older * older): # closer
                print('Your most recent guess was closer to my number than your previous guess, and too low.')
                player = input('You\'ve guessed ' + str(guess) + ' times. Pick a number between ' + str(low) + ' and ' + str(high) + ':')
                if player.lower() == 'done':  # player quit
                    print('You gave up after ' + str(guess) + ' guesses. My number was ' + str(comp) + '.')
                    game = 'over'
                    break
                player = int(player)
                if player < low or player > high:  # player out of range
                    print('Can\'t figure out how a range works, eh? We\'re done here.')
                    game = 'over'
                    break
                older = old
                old = player
                guess += 1
            else: # same distance
                print('Your most recent guess was same distance from my number as your last guess, and too low')
                player = input('You\'ve guessed ' + str(guess) + ' times. Pick a number between ' + str(low) + ' and ' + str(high) + ':')
                if player.lower() == 'done':  # player quit
                    print('You gave up after ' + str(guess) + ' guesses. My number was ' + str(comp) + '.')
                    game = 'over'
                    break
                player = int(player)
                if player < low or player > high:  # player out of range
                    print('Can\'t figure out how a range works, eh? We\'re done here.')
                    game = 'over'
                    break
                older = old
                old = player
                guess += 1

        # guess too high
        elif player > comp and guess > 1:
            if (old * old) > (older * older): # further
                print('Your most recent guess was further from my number than your previous guess, and too high.')
                player = input('You\'ve guessed ' + str(guess) + ' times. Pick a number between ' + str(low) + ' and ' + str(high) + ':')
                if str(player).lower() == 'done':  # player quit
                    print('You gave up after ' + str(guess) + ' guesses. My number was ' + str(comp) + '.')
                    game = 'over'
                    break
                player = int(player)
                if player < low or player > high:  # player out of range
                    print('Can\'t figure out how a range works, eh? We\'re done here.')
                    game = 'over'
                    break
                older = old
                old = player
                guess += 1
            elif (old * old) < (older * older): # closer
                print('Your most recent guess was closer to my number than your previous guess, and too high.')
                player = input('You\'ve guessed ' + str(guess) + ' times. Pick a number between ' + str(low) + ' and ' + str(high) + ':')
                if str(player).lower() == 'done':  # player quit
                    print('You gave up after ' + str(guess) + ' guesses. My number was ' + str(comp) + '.')
                    game = 'over'
                    break
                player = int(player)
                if player < low or player > high:  # player out of range
                    print('Can\'t figure out how a range works, eh? We\'re done here.')
                    game = 'over'
                    break
                older = old
                old = player
                guess += 1
            else: # same distance
                print('Your most recent guess was same distance from my number as your last guess, and too high')
                player = input('You\'ve guessed ' + str(guess) + ' times. Pick a number between ' + str(low) + ' and ' + str(high) + ':')
                if player.lower() == 'done':  # player quit
                    print('You gave up after ' + str(guess) + ' guesses. My number was ' + str(comp) + '.')
                    game = 'over'
                    break
                player = int(player)
                if player < low or player > high:  # player out of range
                    print('Can\'t figure out how a range works, eh? We\'re done here.')
                    game = 'over'
                    break
                older = old
                old = player
                guess += 1

    # victory at sea
    if player == comp:
        print('How was that for you? It took you ' + str(guess) + ' guesses to get my number.')
        game = 'over'

# player game type fail
if game == 'over':
    print('Game Over. Please rate us on the app store.')

if game != 'overlord' and game != 'guesser' and game != 'over':
    print('Game type "' + game + '" is only included in the paid DLC.')