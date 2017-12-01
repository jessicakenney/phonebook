#!/usr/bin/python3.6

# This will contain a "Contact" class with at-least the following properties:
# Name, number, address, note
#
# Be able to use the Python3.6 interpreter to import your module and create Contact instances
# Then create a Phonebook module that imports your Contact class and uses an interface
# to save and list all Contacts in memory.
#
# Additionally, have a search function that can accept at-least a 'name' parameter.
#
# Then, if you're comfortable in your Python databasing skills:
# *** (you might want to wait for this section until you get familiar with docker
# and mariadb later in this section) ***
# Create a database manager module
# Have CRUD functionality for your Contact class
# Save this project in a safe place, we will revisit in the Flask section!

import sys
from contact import Contact

def create_from_file():
    print ('Creating phonebook from contact.txt')
    fh = open('contact.txt','r')
    properties = dict()
    contacts=dict()
    for line in fh.readlines():
        pairs = line.split(',')
        for pair in pairs:
            words = pair.split(":")
            key = words[0]
            value = words[1]
            properties[key]= value
        new_contact = Contact(**properties)
        #Database free version, create dict with name key
        contacts[new_contact.get_variable('name')] = new_contact
    return contacts

def create_contacts():
    contacts = {}
    properties0 = dict( name =  'Jessica Sheridan', number =  '503 - 209 - 2162', address = '123 Main Street', note = 'friend')
    contact0 = Contact(**properties0)
    contacts[contact0.get_variable('name')] = contact0
    properties1 = dict( name =  'Sarah Brakstad', number =  '5167996544', address = '2067 Oak Street', note = 'cousin')
    contact1 = Contact(**properties1)
    contacts[contact1.get_variable('name')] = contact1
    return contacts

def list(contacts):
    for contact in contacts.keys():
        print(contact.upper())
        print(contacts[contact].get_variable('number'))
        print(contacts[contact].get_variable('address'))
        print(contacts[contact].get_variable('note'))
        print('----------------')

def search_name(contacts,name):
    import re
    print('Searching for... ',name)
    #print('keys',contacts.keys())
    found = 0
    for contact in contacts.keys():
        if re.search(name, contact, re.IGNORECASE) :
            found = 1
            match = contacts[contact]
    if (found == 1) :
        print("Found : ",match.get_variable('number'))
    else:
        print("Did not find : ",name)

def remove_contact(contacts,name):
    import re
    for contact in contacts.keys():
        if re.search(name, contact, re.IGNORECASE) :
            print("removing...",name)
            contacts.pop(contact,None)
            break
    list(contacts)
    return contacts

def main():
    import sys
    if len(sys.argv) == 1:
        print ("Usage: -find <name> -list -delete <name>")
        sys.exit(1)
    else:
        arguments = sys.argv[1:]
        print("Args: ",arguments)
        contacts = create_from_file()
        #contacts = create_contacts()

    if (arguments[0] == '-create') :
        pass
    elif (arguments[0] == '-list') :
        list(contacts)
    elif (arguments[0] == '-find') :
        search_name(contacts,arguments[1])
    elif (arguments[0] == '-remove') :
        remove_contact(contacts,arguments[1])

    print('Done.')


if __name__== "__main__": main()

