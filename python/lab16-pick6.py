'''
lab 16: pick 6
'''
import random

# create ticket with definable range parameters
def pick_six (low, high):
    pix = []
    i = 0
    while i < 6:
        check = random.randint(low, high)
        # prevent repeated choices on same ticket
        while check in pix:
            check = random.randint(low, high)
        pix.append(check)
        i += 1
    return pix

# user input for number of random tickets purchased and range of numbers used by game
runs = int(input('How many times would you like me to invest for you?'))
print('Next, we\'ll define the range for your number choices.')
low = int(input('What is the bottom of your number range?'))
high = int(input('What is the top of your number range?'))

winner = pick_six(low, high)    # create winning ticket
win_table = [0, 4, 7, 100, 50000, 1000000, 25000000]    # values for correct matches per ticket

# earnings, cost, and run variables initiated
earnings = 0
cost = 0
i = 0

# simulated ticket play with same winning ticket & user defined number of runs
while i < runs:
    gamble = pick_six(low, high)    # generate new random ticket for run
    match = 0   # track matches per ticket
    read = 0    # used to cycle through indices of winning ticket

    # check/track matches per ticket, track cost, determine winnings per ticket, progress to next run(i)
    for ticket in gamble:
        if ticket == winner[read]:
            match += 1
        read += 1
    cost += 2
    earnings += win_table[match]
    i += 1

# display cost, winning, ROI
print('Cost = $' + str(cost))
print('Winnings = $' + str(earnings))
print('ROI = ' + str((earnings - cost) / cost ))