'''
lab 27 - contact list
'''

contacts = []    # list containing contact dictionaries
keys = []    # list of keys for each dictionary
temp = 'BLANK'    # used for initial key generation and value holder for dict creation
feed = {}    # used to create and pass dict for each user
working = {}    # used to track current contact
current_index = 0
mode = ''    # mode switch variable

# function iterates through dictionaries, compares chosen value to value attached to name key, returns dict if found
def retrieve_dict (mode):
    temp = input('What is the name of the contact you\'d like to ' + mode + '?:')    # prompt for name choice
    while temp != 'done':    # loop repeats until match found, or input "done"
        for i in contacts:
            if i['name'].lower() == temp.lower():    # if match found, save dict to working, present info, break iteration loop
                working = i
                print('Here is the information for ' + temp + ':')
                print(working)
                temp = 'skip'
                break
        if temp != 'skip':    # if match not found, show entered value, prompt for new
            print(temp + ' not found.')
            temp = input('Enter "done", or choose new contact:')
        else:
            temp = 'done'    # exit while loop
    return working    # return working dict

# instructions, input csv filename, initiate mode variable
print('The following program allows you to access and alter your contact list.')
print('If you\'d like to exit the program at any point, input "done" using the console.')
csv = input('What is the name of the CSV file?(full path may be needed):') or 'contactlab27.txt'

with open(csv, 'r') as file:  # open file for reading, split into elements of list using \n as EOL identifier
    lines = file.read().split('\n')

for i in lines:  # iterate through elements
    if temp == 'BLANK':  # keygen check, create keys list
        keys = i.split(',')
        temp = []
    else:  # create contact dictionaries, create list of dictionaries
        temp = i.split(',')
        for j in keys:  # iterate through keys, assign values
            feed[j] = temp.pop(0)
            if j == keys[-1]:  # add dictionary to list, reset feed dict
                contacts.append(feed)
                feed = {}
                temp = ''

while mode != 'done':

    # description of modes and user choice prompt
    mode = input('To input new contact & attributes, type "create"\n'
                 'To retrieve contact info, type "retrieve"\n'
                 'To update contact info, type "update"\n'
                 'To delete a contact, type "delete"\n'
                 'What would you like to do?:')

    if mode.lower() == 'create':  # add contact info
        for j in keys:  # iterate through keys
            temp = input('What is the ' + j + ' for the contact?:')  # user input values
            if temp == 'done':
                mode = 'done'
                break
            feed[j] = temp  # populate contact dictionary
            if j == keys[-1]:
                contacts.append(feed)  # add complete contact dict to list
                feed = {}  # reset feed variable

    # retrieve mode uses retrieve function
    elif mode.lower() == 'retrieve':
        working = retrieve_dict(mode)

    # update mode uses current data or retrieves, prompt for field(key) value to update
    elif mode.lower() == 'update':
        if working != {}:    # if working dict not blank, prompt user if current data desired for update
            temp = input('Enter "yes" if you have the correct contact information:')
        if temp.lower() != 'yes':    # retrieve new contact using retrieve function
            working = retrieve_dict(mode)
        while mode == 'update':
            print('Choose which of the following fields you\'d like to update:')    # identify keys and prompt user
            temp = input(keys).lower()
            if temp in keys:    # preview current data and prompt user for update
                print(temp.upper() + ' is currently set to ' + working[temp] + '.')
                working[temp] = input('Enter updated information, or leave blank to leave unchanged:') or working[temp]
                print(temp.upper() + ' is now set to ' + working[temp] + '.')
            else:
                print(temp + ' is not a valid field for update.')    # inform user of invalid choice
            mode = input('You can continue to "update" current contact,\n'
                         'or you can choose "create", "retrieve", "delete", or "done":').lower()    # continue update or new mode

    # delete mode removes contact dict from contacts list
    elif mode.lower() == 'delete':
        if working != {}:    # prompt user if working dict not blank
            temp = input('Enter "yes" if you have the correct contact information:')
        if temp.lower() != 'yes':    # retrieve contact dict using function
            working = retrieve_dict(mode)
        temp = input('Enter "continue" to delete the contact:')    # verify before delete, remove dict from contacts list if true
        if temp.lower() == 'continue':
            contacts.remove(working)

# build CSV list from contacts list, preview and save list
temp = input('Enter "finalize" to preview and save contact list as CSV file:')
if temp.lower() == 'finalize':
    csv = ''
    for i in keys:    # iterate through keys and save to top of CSV file
        csv += i
        if i == keys[-1]:
            csv += '\n'
        else:
            csv += ','
    for dict in contacts:    # iterate through dicts and keys, add values to CSV file, new dict is new line
        temp = len(keys)
        for field in dict:
            temp -= 1
            csv += dict[field]
            if temp == 0:
                csv += '\n'
            else:
                csv += ','
    print('Following is a preview of your contacts CSV file:')    # preview of final CSV
    print(csv)
    temp = input('Enter "save" to save CSV file:')
    if temp.lower() == 'save':
        save_name = input('Enter desired filename for saving CSV contact list:')    # prompt user for filename and save
        with open(save_name, 'w') as prepare_csv:
            prepare_csv.write(csv)
        print('CSV contact list saved, send someone their favorite fruit.')    # tell user to make contact with another human using fruits

else:
    print('All done, go play outside.')    # tell user to go outside, immediately!