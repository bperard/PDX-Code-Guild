'''
lab 25 - taking words and making numbers
'''
# ## top ten word counts
# # open text for reading, add to contents variable
# with open('Commonsense.txt', 'r') as f:
#     contents = f.read()
#
# # all characters to ignore in count
# skip = ['â','„','¢','','¿','»','ï',',','"',';',':','.','?','!','(',')','<','>','^','*','#','%','+','@','/','\\','{','}','[',']','~']
#
# # create words dict: keys are words, elements are count
# words = {}
# check = ''
# for i in contents:    # iterate through each char in file
#     if i in skip:    # disregard chosen chars
#         continue
#     elif i == ' ' or i == '\n':    # identify words by separating strings at breaks and spaces
#         if check in words:    # tally repeated word and reset check variable
#             words[check] += 1
#             check = ''
#         elif check == '':    # disregard blank check in count
#             continue
#         else:    # add new word and tally to words dict, reset check
#             words[check] = 1
#             check = ''
#     else:    # feed check new char from file and lower case
#         check += i.lower()
#
# fix = list(words.items())    # convert words dict to list fix with nested list elements [word, count]
# top_counts = [[0,0]]    # list for storing sorted top counts
# for i in fix:    # iterate through list elements
#     if len(top_counts) < 10:
#         for j in top_counts:    # sort and store ordered count with related word
#             if i[1] > j[0]:
#                 top_counts.insert(top_counts.index(j), [i[1], i[0]])
#                 break    # break loop if requirements met to add new element
#     else:
#         for j in range(0, 10):    # limit check to top ten counts, storing ordered element if requirements met
#             if i[1] >= top_counts[j][0]:
#                 top_counts.insert(j, [i[1], i[0]])
#                 break
#
#
# if len(top_counts) < 11:    # remove initial empty placeholder
#     for i in top_counts:
#         if i == [0,0]:
#             top_counts.remove(i)
# elif len(top_counts) > 10:    # remove words with a count less than the tenth element
#     for i in range(10, len(top_counts) - 1):
#         if top_counts[9][0] > top_counts[i][0]:
#             top_counts = top_counts[0:i]
#             break
#
# for i in top_counts:    # print information for top counts
#     print(str(i[0]) + ' uses of "' + i[1] + '"')

## top ten word pairs and chosen word pairs
# open text for reading, add to contents variable
with open('Commonsense.txt', 'r') as f:
    contents = f.read()

# all characters to ignore in count
skip = ['â','„','¢','','¿','»','ï',',','"',';',':','.','?','!','(',')','<','>','^','*','#','%','+','@','/','\\','{','}','[',']','~']

# create word_pairs dict: keys are word pairs, elements are count
word_pairs = {}
check = ''
lead = 'BLANK'
for i in contents:    # iterate through each char in file
    if i in skip:    # disregard listed chars
        continue
    elif i == ' ' or i == '\n':    # identify words by separating strings at breaks and spaces
        if lead == 'BLANK':    # disregard placeholder pair and set lead
            lead = check
            check = ''
        else:
            pair = str(lead) + ' ' + str(check)
            if check == '':  # disregard blank check in count
                continue
            elif pair in word_pairs:    # tally repeated word pair, set lead and reset check variables
                word_pairs[pair] += 1
                lead = check
                check = ''
            else:  # add new word pair and tally to word_pairs dict, set lead and reset check
                word_pairs[pair] = 1
                lead = check
                check = ''
    else:    # feed check new char from file and lower case
        check += i.lower()

fix = list(word_pairs.items())    # convert word_pairs dict to list fix with nested list elements [word, count]

# allow user to see top pairs, or chosen pairs
user = input('Enter "top" to see top ten word pair counts, or\n'
             'enter "chosen" to see frequency of words following your selection:')

# user fail
if user.lower() != 'top' and user.lower() != 'chosen':
    print(user + ' was not a listed choice; this is why we can\'t have nice things.')

# choose word and create list of chosen pairs
elif user.lower() == 'chosen':
    sel_pairs = []    # store new pairs
    chosen = input('What word would you like to see pairs of?:').lower()
    for i in fix:    # iterate through elements in fix to find chosen pairs
        run = i[0]
        build = ''
        for j in run:    # check for chosen leading pair, add to sel_pairs if present, skip to next pair if not, use ' ' to determine word break
            if j == ' ' and build == chosen:
                sel_pairs.append(i)
                build = ''
                break
            elif j == ' ':
                build = ''
                break
            build += j
    if sel_pairs == []:    # notify of no matching pairs
        print('There are no pairs leading with ' + chosen + ' in the text.')
    fix = sel_pairs    # feed chosen pair list to top ten pairs functionality

# top ten word pairs in text and chosen pair top ten
if user.lower() == 'top' or user.lower() == 'chosen':
    top_counts = [[0, 0]]  # list for storing sorted top counts
    for i in fix:  # iterate through list elements
        if len(top_counts) < 10:
            for j in top_counts:  # sort and store ordered count with related word pair
                if i[1] > j[0]:
                    top_counts.insert(top_counts.index(j), [i[1], i[0]])
                    break  # break loop if requirements met to add new element
        else:
            for j in range(0, 10):  # limit check to top ten counts, storing ordered element if requirements met
                if i[1] >= top_counts[j][0]:
                    top_counts.insert(j, [i[1], i[0]])
                    break

    if len(top_counts) < 11:  # remove initial empty placeholder
        for i in top_counts:
            if i == [0, 0]:
                top_counts.remove(i)
    elif len(top_counts) > 10:  # remove word pairs with a count less than the tenth element
        for i in range(10, len(top_counts)):
            if top_counts[9][0] > top_counts[i][0]:
                top_counts = top_counts[0:i]
                break

    for i in top_counts:  # print information for top counts
        print(str(i[0]) + ' uses of "' + i[1] + '"')

