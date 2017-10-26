'''
lab 14 practice problems
'''
#
# # problem 1: string letter counter
#
# def count_letter (char, word):
#     count = 0
#     for letter in word:
#         if letter != char:
#             continue
#         else:
#             count += 1
#     return count
#
# # problem 2: lowered no space
#
# def lower_case(word):
#     word = word.lower().strip()
#     return word
#
# # problem 3: even?
#
# def is_even (num):
#    return num % 2 == 0
#
# # problem 4: random element
#
# def random_element (list):
#     import random
#     return list[random.randint(0, len(list) - 1)]
#
# # problem 5: max parameter
#
# def max_para (a, b, c):
#     if a > b:
#         max = a
#     else:
#         max = b
#     if max < c:
#         max = c
#     return max
#
# # problem 6: the power of two
#
# def two_up (x, low, high):
#     i = low
#     while i <= high:
#         powers = x ** i
#         i += 1
#         print(powers)
#
# # problem 7: max, min, mean, mode*
#
# def max_list (list): # return list max
#     max = list[0]
#     for i in list:
#         if i > max:
#             max = i
#     return max
#
# def min_list (list): # return list min
#     min = list[0]
#     for i in list:
#         if i < min:
#             min = i
#     return min
#
# def mean_list (list): # return list mean
#     total = 0
#     for i in list:
#         total += i
#     return total / len(list)

###########Return to mode
# x = [123,-8,-8,0,34563,2,3568,3,234,4,4,4, -23,23]
# # y = ['apples', 'pears', 'grapes', 'lemons']
#
# # sort list to order matches
# list = x.sort()
# #
# # # intitiate list to track number(s) with highest occurrence(s)
# # result = [0]
# # print(result)
# # # insert foreign element to list for initial check
# # result.insert(1, (x[0] - 1))
# # print(result)
# # # list for reset and counter
# # fresh = []
# # count = 0
# #
# # for i in x: # cycle through list
# #
# #     if result[1] == i: # check for matching elements
# #         count += 1     # increase element iteration tracker
# #     else:
# #         count = 1       # start/reset iteration tracker
# #
# #     if count == result[0]:        # build mode list
# #         result.insert(1, i)
# #     elif count > result[0]:# create new list for greater occurrence
# #             result = [count, i]
# print(list[1:]) remove counter nvm string

# # problem 8: reverse
# x = ['apple', 3, 'toad']
# def rev_list (list):
#     list.reverse()
#     return list

# problem 9: return shared list

def list_share (lisa, lisb):
    shared = []
    for i in lisa:
        if i in lisb:
            print(i)
#             shared.append(i)
#     return shared

# # problem 10: return list with elements less than n
#
# def less_than (list, n):
#     here = []
#     for i in list:
#         if i < n:
#             here.append(i)
#     return here

# # problem 11: combine and alternate two lists equal length
#
# def list_comb (lisa, bart):
#     sexyflanders = []
#     for i in range(len(lisa)):
#         sexyflanders.append(lisa[i])
#         sexyflanders.append(bart[i])
#     return sexyflanders

# # problem 12: combine all
#
# def combine_all(nested):
#     freed = []
#     for list in nested:
#         for element in list:
#             freed.append(element)
#     return freed

# # problem 13:
#
# def fibonacci(n):
#     fibp = 0
#     fibc = 1
#     if n == 0:
#         return 0
#     for i in range(n-1):
#         temp = fibc
#         fibc = fibp + fibc
#         fibp = temp
#     return fibc

# # problem 14:

def latest_letter(feed):
    full = 'abcdefghijklmnopqrstuvwxyz'
    max = 0
    for i in feed.lower():
        temp = full.find(i)
        if temp > max:
            max = temp
            latest = i
    if max == 0:
        return 'no valid letters'
    return latest