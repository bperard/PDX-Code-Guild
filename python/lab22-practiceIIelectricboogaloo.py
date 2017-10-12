'''
lab 22 - Practice Problems II: Electric Boogaloo
'''

# # 01 - REPL after me
#
# check = ''
# here = []
# while check != 'done':
#     check = input('Enter a number (or "done"):').lower()
#     if check == 'done':
#         break
#     else:
#         here.append(int(check))
# print(here)
#
# # # 02 - Every other
#
# def while_other (list):
#     i = 0
#     while i < len(list):
#         if i % 2 == 0:
#             print(list[i])
#         i += 1
#
# def for_other (list):
#     for i in range(len(list)):
#         if i % 2 == 0:
#             print(list[i])
#
# # 03 the target of my target is our sum (that doesn't work)
#
# # intro and variable initiate
# print('Enter a list of numbers and a target number.\n'
#       'If possible, I\'ll find a pair from your list whose sum is your target number.')
# nums = []
# check = ''
#
# # looping input for int list creation and user target input
# while check != 'done':
#     check = input('Enter a number (or "done"):').lower()
#     if check == 'done':
#         break
#     else:
#         nums.append(int(check))
# target = int(input('Enter a target number:'))
#
# def pair_sum (nums, target):    # check and print pair with sum of target
#     sum = ['x']    # check for no possible pairs
#     for i in nums:    # loop through all pairs, terminate if pair with target sum found
#         for x in nums:
#             if i + x == target:
#                 sum = [i, x]
#                 break
#         if i + x == target:
#             break
#
#     if sum[0] == 'x':    # no pairs found output
#         print('No pairs in your list have a sum of ' + str(target) + '. This makes me super sad.')
#     else:    # pair found output
#         print('A pair from your list with a sum of ' + str(target) + ' is:')
#         print(sum)
#
# # 04 - it's starting to look like a triple string
#
# double = input('I am a robot who eats your text and gives you back twice as much.\n'
#                'FEED ME!!!:')
# rad = ''
# for i in double:
#     rad += i
#     rad += i
# print(rad)
# print('Aren\'t computers RAD!?!')
#
# # 05 - two lists enter, one list leaves
#
# lisa = [2,5,7,5]
# bart = [3,4,2,6]
#
# def list_list (lisa, bart):
#     maggie = []
#     if len(lisa) != len(bart):
#         return 'Worst episode ever.'
#     for i in range(len(lisa)):
#         maggie.append([lisa[i], bart[i]])
#     return maggie
#
# # 06 - duality check
#
# def duality_check (a, b):
#     check = 'neg'
#     if a > 0:
#         check = 'pos'
#     if check == 'neg' and b > 0:
#         return True
#     elif check == 'pos' and b < 0:
#         return True
#     else:
#         return False
#
# # 07 - within ten (starring Keanu Reeves)



