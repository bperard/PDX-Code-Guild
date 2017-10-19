'''
lab 27 - contact list
'''
# open file for reading, split into elements of list using \n as EOL identifier
with open('contactlab27.txt', 'r') as file:
    lines = file.read().split('\n')
contacts = []    # list containing contact dictionaries
keys = []    # list of keys for each dictionary
temp = 'BLANK'    # used for initial key generation and value holder for dict creation
feed = {}    # used to create and pass dict for each user

for i in lines:    # iterate through elements
    if temp == 'BLANK':    # keygen check, create keys list
        keys = i.split(',')
        temp = []
    else:    # create contact dictionaries, create list of dictionaries
        temp = i.split(',')
        for j in keys:    # iterate through keys, assign values
            feed[j] = temp.pop(0)
            if j == keys[-1]:    # add dictionary to list, reset feed dict
                contacts.append(feed)
                feed = {}

print(contacts)