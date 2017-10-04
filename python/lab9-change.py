'''
Making change
'''
# declaring coin values
quarters = 25
dimes = 10
nickles = 5
pennies = 1

# user input, converted to float
change = float(input('Giving proper change is key to getting ahead in this crazy world.\n'
                     'How much money do you have? (for accurate results, use #.## format)'))

# convert float to int for math
change = int(change * 100)

# proper coinage math
#first line determins amount, second passes remaining change forward
quarters = int(change // quarters)
change -= quarters * 25

dimes = int(change // dimes)
change -= dimes * 10

nickles = int(change // nickles)
change -= nickles * 5

pennies = int(change // pennies)

# print proper coinage
print('Proper change is: ' + str(quarters) + ' quarters, ' + str(dimes) + ' dimes, ' + str(nickles) + ' nickles, and ' + str(pennies) + ' pennies.')