'''
lab 19 palindrome/anagram check
'''

# return whether parameter is a palindrome
def pali_chk (pals):
    return pals == pals[::-1]

# return whether words are anagrams

# strip spaces and string to sorted list
def string_sort_list (feed):
    feed = feed.replace(' ','')    # strip spaces
    out =[]
    for i in feed:    # 'feed' string to 'out' list
        out.append(i)
    out.sort()    # sort list
    return out

# user input strings
first = input('What is the first word or phrase?')
second = input('What is the second word or phrase?')

# run strip/list/sort function, compare, output anagram status
if string_sort_list(first) == string_sort_list(second):
    print(first + ' and ' + second + ' are anagrams')
else:
    print(first + ' and ' + second + ' aren\'t anagrams')


