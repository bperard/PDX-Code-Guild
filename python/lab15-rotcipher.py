'''
lab 15: rot cipher
'''

# unaltered alpha reference
alpha = 'abcdefghijklmnopqrstuvwxyz'

# change str into iterable list
def string_list (feed):
    out =[]
    for i in feed:    # 'feed' string to 'out' list
        out.append(i)
    return out

# user input string to encrypted/decrypted string of chosen rotation
def output_string (user, rot):
    cipher = ''
    for i in user:
        if i in alpha:
            if mode == 'encrypt':
                # change each string char into alpha index, shift by input rot, change to encrypted char
                cipher += alpha[(string_list(alpha).index(i) + rot) % 26]
            if mode == 'decrypt':
                # change each string char into alpha index, shift forward by 26 (length of alpha) - rot, change to decrypted char
                cipher += alpha[(string_list(alpha).index(i) + (26 - rot)) % 26]
        else:
            # leave non-alpha chars untouched and in position
            cipher += i
    return cipher

print('This program will encrypt and decrypt any message using alpha rotation.')    # intro
user = input('What is the message?').lower()    # input string
rot = int(input('What is the key rotation?'))    # input rot for encrypt/decrypt

mode = input('Would you like to "encrypt" or "decrypt" the message?').lower()    # encrypt/decrypt selection and user error correction
if mode != 'encrypt' and mode != 'decrypt':
    input('Please select "encrypt" or "decrypt" to continue.').lower()

print(output_string(user, rot))    # output encrypted/decrypted string


