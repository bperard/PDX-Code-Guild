'''
Input and average list of numbers
'''

# variables
user = None
numbers = []
total = 0
average = None

# instructions
print('Feed me numbers until you grow weary. Once the fatigue sets in,\n'
      'type "done" and I will feed you their average.')

# user input into list
while user != 'done':
    user = input('Feed me a number, or tell me you\'re done.').lower()
    numbers.append(user)

# add user inputs
for i in range(len(numbers) - 1):
    total += int(numbers[i])

# average user inputs
average = total / len(numbers)

# give user average
print('Your average is: ' + str(average))