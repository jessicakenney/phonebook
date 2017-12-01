#!/usr/bin/python3.6

from phonebook import Phonebook
from contact import Contact


def create_from_file():
    print ('Creating phonebook from contact.txt\n')
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

def main():
    import sys
    if len(sys.argv) == 1:
        print ('Usage: app.py -list \n -find <name> \n -delete <name>')
        sys.exit(1)
    else:
        arguments = sys.argv[1:]
        print("Args: ",arguments)
        contacts = create_from_file()
        phonebook = Phonebook(contacts)
    if (arguments[0] == '-list') :
        phonebook.list()
    elif (arguments[0] == '-find') :
        phonebook.search_name(arguments[1])
    elif (arguments[0] == '-remove') :
        phonebook.remove_contact(arguments[1])
    else :
        print ('Usage: app.py -list \n -find <name> \n -delete <name>')
        sys.exit(1)

    print('Done.')

if __name__ == "__main__": main()