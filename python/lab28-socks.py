'''
lab 28 socks
'''

import random    # used for randint

# lists for color and type, pile list, drawer dict
sock_colors = ['black', 'white', 'blue']
sock_types = ['ankle', 'crew', 'calf', 'thigh']
sock_pile = []
sock_drawer = {}

# generate random sock pile list with tuple (color, type)
while len(sock_pile) < 100:
    sock_pile.append((sock_colors[random.randint(0,2)], sock_types[random.randint(0,3)]))

# sort sock tuples into sorted drawer dict, new type creates key with 1 value, found key increments value by one
for sock in sock_pile:
    if sock in sock_drawer:
        sock_drawer[sock] += 1
    else:
        sock_drawer[sock] = 1

# sorted sock key values changed to pairs (value // 2) and noted if loner exists (value % 2)
for sorted in sock_drawer:
    if sock_drawer[sorted] % 2 == 0:
        sock_drawer[sorted] = str(sock_drawer[sorted] // 2) + ' pairs & no loner'
    else:
        sock_drawer[sorted] = str(sock_drawer[sorted] // 2) + ' pairs & a loner'

print(sock_drawer)