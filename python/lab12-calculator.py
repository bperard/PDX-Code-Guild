'''
lab 12 - Math for hire
'''

# instructions
print('Lost your phone? let me be your calculator.\n'
      'I can perform math, compare numbers, and determine whether something is true or false.\n'
      'When you are mathed out, simply input "done."')

# input variables
operation = None
numa = None
numb = None

# collect and evaluate user input
while True:
    operation = input('What operation would you like to perform?').lower()
    if operation == 'done': # exit check
        break # exit loop
    numa = input('What is your first number?').lower()
    if numa == 'done':
        break
    numb = input('What is your second number?').lower()
    if numb == 'done':
        break
    print(numa + ' ' + operation + ' ' + numb + ' = ' +str(eval(numa + operation + numb))) # output answer

print('Goodbye!')
