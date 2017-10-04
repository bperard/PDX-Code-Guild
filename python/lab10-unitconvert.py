'''
Converting given units to desired units
'''

# conversion list
conversion = [.0254, .3048, .9144, 1, 1000, 1609.34]

# corresponding units for conversion
units = ['inch', 'ft', 'yard', 'm', 'km', 'mi']

# user input
print('Let me convert a distance for you. Acceptable units are:\n'
      'inch, ft, yard, m, km, mi')
distance = float(input('What is the given distance?'))
given = input('What are the units of the given distance?')
desired = input('Which units would you like the given distance converted to?')
print('Beep,boop; I live my life a quarter mile at a time.')

if given in units and desired in units:

    # conversion to meters
    meters = (conversion[units.index(given)]) * distance

    # conversion to desired
    result = meters / conversion[units.index(desired)]

    # solution
    print(str(distance) + given + ' is equal to ' + str(result) + desired)

# fail
else:
    print('You had one job...')