'''
lab 20 credit card validation
'''

# intro, user input, create list variable
print('This program will validate whether or not a string of numbers passes credit card validation.\n'
      'Your trust is important to us, so we promise not to save any and all numbers input into this system.\n'
      '... at least we\'re pretty sure we won\'t.')
user = input('Enter the card number for validation:')
list = []

# user input string to list of int, spaces removed
for char in user:
    if char == ' ':
        continue
    else:
        list.append(int(char))

# remove check digit from end of list, reverse list
check = list.pop(-1)
list.reverse()

# iterate through list indices: multiply every other element by 2,
# subtract 9 from elements > 9, and sum all elements
i = 0
sum = 0
while i < len(list):
    if i % 2 == 0:
        list[i] *= 2
        if list[i] > 9:
            list[i] -= 9
    sum += list[i]
    i += 1

# compare check and second digit of sum for validation
if check == int(str(sum)[1]):
    print('Card number has been validated, but also reported as stolen.\n'
          'To resolve this situation, provide your electronic signature below.\n'
          'Your card will be charged a small $101 processing fee to verify you aren\'t a thief.\n'
          'If fee is not paid, we will be forced to send the nearest FBI office to you.')
else:
    print('This card number is worthless, stop wasting our time.')


# as a function with boolean return

def credit_card_check (creditnumb):
    list = []
    # parameter "user" string to list of int, spaces removed
    for char in creditnumb:
        if char == ' ':
            continue
        else:
            list.append(int(char))
    # remove check digit from end of list, reverse list
    check = list.pop(-1)
    list.reverse()
    # iterate through list indices: multiply every other element by 2,
    # subtract 9 from elements > 9, and sum all elements
    i = 0
    sum = 0
    while i < len(list):
        if i % 2 == 0:
            list[i] *= 2
            if list[i] > 9:
                list[i] -= 9
        sum += list[i]
        i += 1
    # compare check and second digit of sum for validation
    return check == int(str(sum)[1])
