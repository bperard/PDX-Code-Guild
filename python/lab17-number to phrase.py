'''
lab 17 number to phrase
'''

# name tables for ones, ten-nineteen, tens
ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ten = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['not used', 'not used', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# user input number
number = int(input('Choose a number between 0 & 999, and I will write it out for you:'))
user = number

# output phrase
numb_out = ''

# hundreds phrase and connector
if (number // 100) > 0:
    numb_out += ones[number // 100]
    numb_out += ' hundred'
    if number % 100 > 0:    # connector check/add
        numb_out += ' and '
    number %= 100    # remove hundreds digit

# tens phrase and connector
if (number // 10) > 0:
    if (number // 10) == 1:    # ten through nineteen
        numb_out += ten[number - 10]
        number = 0
    else:
        numb_out += tens[number // 10]
        if number % 10 > 0:    # connector check/add
            numb_out += '-'
        number %= 10    # remove tens digit

# ones phrase and zero
numb_out += ones[number]
if numb_out == '':
    numb_out = 'zero'

# output
print(numb_out)