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
#
# and mariadb later in this section) ***
# Create a database manager module
# Have CRUD functionality for your Contact class
# Save this project in a safe place, we will revisit in the Flask section!

from contact import Contact

def main():
    fh = open('contact.txt','r')
    properties = dict()
    for line in fh.readlines():
        words = line.split()
        print(words)
        key = words.pop(0)
        value = ' '.join(words)
        print('KEY: ',key)
        print('Value: ',value)
        properties[key]= value
    print (properties)
    new_contact = Contact(**properties)
    print('Name',new_contact.get_variable('Name'))
    print('Done.')


if __name__== "__main__": main()

