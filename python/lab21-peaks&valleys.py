'''
lab 21 peaks and valleys
'''

# intro and user input number string
print('This program will create a topographical chart from a string of numbers.\n'
      '"0" and "9" represent the lowest and highest points possible.\n'
      'Information will be provided for peaks, valleys, and plateaus.')
topography = input('Enter desired number string:')

# initiate chart list, convert string to int elements within chart
chart = []
for rocks in topography:
    chart.append(int(rocks))

# initiate tracker variables peak, valley, plateau
peak = []
valley = []
plateau = []

# initiate variable to track max peak height(pheight) index/indices(ploc)
pheight = 0
ploc = []

# check for initial plateau
if chart[0] == chart[1]:
    plateau.append(0)

# determine indices for peaks, valleys, and plateaus
i = 1
while i < (len(chart) - 1 ):
    if chart[i] > chart[i - 1] and chart[i] > chart[i + 1]:    # peak check and index save
        peak.append(i)
        if chart[i] > pheight:    # new max peak check
            pheight = chart[i]    # set new max height
            ploc = [i]            # save peak index
        elif chart[i] == pheight:    # check for equal to max peak
            ploc.append(i)           # save equal peak index
    elif chart[i] < chart[i - 1] and chart[i] < chart[i + 1]:    # valley check and index save
        valley.append(i)
    if chart[i] == chart[i + 1]:    # plateau check and index save; also max/equal peak checks
        plateau.append(i)
        if chart[i] > pheight:
            pheight = chart[i]
            ploc = [i]
        elif chart[i] == pheight:
            ploc.append(i)
    elif chart[i] == chart[i - 1]:
        plateau.append(i)
        if chart[i] == pheight:
            ploc.append(i)
    i += 1

# check for ending plateau
if chart[-1] == chart[-2]:
    plateau.append(len(chart) - 1)

# unnecessary due to peak check, saving for possible use
# # initiate tracker for wet plateau check, edge location, and wet plateau index store
# chain = 'b'
# edge = None
# wetplat = []
#
# # determine if plateau holds water, if so, store wet plateau edge coordinates
# for map in range(len(chart)):
#     if map in plateau:
#         if chart[map] < chart[map - 1]:
#             chain = 'W'
#             edge = map
#         elif chart[map] < chart[map + 1]:
#             if chain == 'W':
#                 wetplat.append([edge, map])
#                 chain = 'b'
#                 edge = None
#         elif chart[map] > chart[map + 1]:
#             if chain == 'W':
#                 chain = 'b'
#                 edge = None





# build topographical map from chart list

# set max height and initiate build string
level = 9
build = ''

# build land and air(adding in water), and set new layers(line break "\n"), top down build pattern
while level > 0:
    for boulder in chart:
        if boulder >= level:
            build += 'X'
        else:
            build += ' '
    build += '\n'
    level -= 1

# build landmark key under map
for map in range(len(chart)):
    if map in peak:
        build += 'P'
    elif map in valley:
        build += 'V'
    elif map in plateau:
        build += '='
    else:
        build += ' '
build += ' <== Landmark Key: (P)eak, (V)alley, (=)Plateau?'

# output data and gui
print('\n')
print('Max peak is at ' + str(ploc) + ' with a height of ' + str(pheight))
print(build)
print('Peaks(P) are located at:')
print(peak)
print('Valleys(V) are located at:')
print(valley)
print('Plateaus(=) are located at:')
print(plateau)

