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
# # problem 7:

def max_list (list):
    max = list[0]
    for i in list:
        if i > max:
            max = i
    return max

x = [123,34563,2,3568,0,234,-454,23]
y = ['apples', 'pears', 'grapes', 'lemons']
def min_list (list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

def mean_list (list):
    total = 0
    for i in list:
        total += i
    return total / len(list)











