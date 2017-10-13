'''
lab 24 - change bogo sort
'''

import random

# random number list with n(umbs) elements function
length = int(input('How many random numbers would you like in your list?:'))
def random_list (length):
    i = 0
    list = []
    while i < length:
        list.append(random.randint(0, 100))
        i += 1
    return list

# iterate through numbs indices and swap each element with another random element in the list
def shuffle (numbs):
    for swap in range(len(numbs)):    # move through indices
        here = random.randint(0, len(numbs) - 1)    # choose random index
        numbs[swap], numbs[here] = numbs[here], numbs[swap]    # swap current index element with random index element

def is_sorted (numbs):
    status = True
    for check in range(len(numbs) - 1):
        if numbs[check] > numbs[check + 1]:
            status = False
    return status

def bogosort (numbs):
    sorted = False
    i = 0
    while sorted != True:
        shuffle(numbs)
        sorted = is_sorted(numbs)
        i += 1
    print(numbs)
    print(i)

list = random_list(length)
bogosort(list)