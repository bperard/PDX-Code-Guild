'''
lab 26 - ARI there yet?
'''
# open text file for reading
feed_txt = input('What file would you like the ARI for?:')
with open(feed_txt, 'r') as f:
    contents = f.read()

# ari_scale dict
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}

# initiate counts and marker lists/variables
skip = ['â','„','¢','','¿','»','ï',',','"',';',':','(',')','<','>','^','*','#','%','+','@','/','\\','{','}','[',']','~']    # ignored characters
sentence = [0,'.','!','?']    # selected markers to identify sentences
word = [1,'\n',' ']    # selected markers to identify words
char = 0
hold = ''    # variable used to prevent increasing word count unnece

for i in contents:
    if i in skip:    # disregard char in skip list
        continue
    elif i in sentence:    # increase sentence count
        sentence[0] += 1
    elif i in word:    # increase word count
        if hold in word:    # prevent extra spacing increasing word count
            i = hold
            continue
        word[0] += 1
        hold = i
    else:    # feed new character
        char +=1
        hold = ''    # reset extra spacing check once qualifying char fed from contents

# calculate ARI, convert to int, reduce if above 14
ARI = int(4.71 * (char / word[0]) + 0.5 * (word[0] / sentence[0]) - 21.43)
if ARI > 14:
    ARI = 14

# output referencing ARI with ari_scale dict
level = 'The ARI for ' + feed_txt + ' is ' + str(ARI) + '.\n'
level += 'This corresponds to a(n) ' + ari_scale[ARI]['grade_level'] + ' level of difficulty\n'
level += 'that is suitable for an average person ' + ari_scale[ARI]['ages'] + ' years old.'
print(level)