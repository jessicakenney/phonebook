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



class Phonebook:

    def __init__(self, contacts):
        self._contacts = contacts

    def list(self):
        for key in sorted(self._contacts):
            print(key.upper())
            print(self._contacts[key].get_variable('number'))
            print(self._contacts[key].get_variable('address'))
            print(self._contacts[key].get_variable('note'))
            print('----------------')

    def search_name(self,name):
        import re
        print('Searching for... ',name)
        found = 0
        for contact in self._contacts.keys() :
            if re.search(name, contact, re.IGNORECASE) :
                found = 1
                match = self._contacts[contact]
        if (found == 1) :
            print("Found : ",match.get_variable('number'))
        else:
            print("Did not find : ",name)
        return found

    def remove_contact(self,name):
        import re
        found = 0
        for contact in self._contacts:
            if re.search(name, contact, re.IGNORECASE) :
                print("Removing...",name)
                print("\n")
                self._contacts.pop(contact,None)
                found = 1
                break
        if (found == 0) :
            print ("Nothing deleted, could not find ",name)
        self.list()
        return self._contacts


