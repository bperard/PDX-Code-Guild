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

# determine indices for peaks, valleys, and plateaus
i = 1
pheight = 0
ploc = []
if chart[0] == chart[1]:
    plateau.append(0)
while i < (len(chart) - 1 ):
    if chart[i] > chart[i - 1] and chart[i] > chart[i + 1]:
        peak.append(i)
        if chart[i] > pheight:
            pheight = chart[i]
            ploc = [i]
        elif chart[i] == pheight:
            ploc.append(i)
    elif chart[i] < chart[i - 1] and chart[i] < chart[i + 1]:
        valley.append(i)
    if chart[i] == chart[i + 1]:
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






level = 9
build = ''
while level > 0:
    for boulder in chart:
        if boulder >= level:
            build += 'X'
        else:
            build += ' '
    build += '\n'
    level -= 1

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


print('\n')
print('Max peak is at ' + str(ploc) + ' with a height of ' + str(pheight))
print(build)
print('Peaks(P) are located at:')
print(peak)
print('Valleys(V) are located at:')
print(valley)
print('Plateaus(=) are located at:')
print(plateau)

