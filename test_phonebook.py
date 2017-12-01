#!/usr/bin/python3.6

from phonebook import Phonebook
from contact import Contact
import unittest

class TestPhonebook(unittest.TestCase):
    def setUp(self):
        self.contacts = dict()
        self.info0 = dict(name='ZuZu',number='123',address='1 Main',note='hi')
        self.info1 = dict(name='Daisy',number='456',address='1 Dog',note='bye')
        self.test_contact0 = Contact(**self.info0)
        self.test_contact1 = Contact(**self.info1)
        self.contacts[self.test_contact0.get_variable('name')] = self.test_contact0
        self.contacts[self.test_contact1.get_variable('name')] = self.test_contact1
        self.test_phonebook = Phonebook(self.contacts)

    def test_newContact(self):
        self.assertEqual(True, type(self.test_contact0) is Contact)

    def test_newContactKwargs(self):
        self.assertEqual('ZuZu', self.test_contact0.get_variable('name'))
        self.assertEqual('123', self.test_contact0.get_variable('number'))
        self.assertEqual('bye', self.test_contact1.get_variable('note'))
        self.assertEqual('1 Dog', self.test_contact1.get_variable('address'))

    def test_newPhonebook(self):
        self.assertEqual(True, type(self.test_phonebook) is Phonebook)

    def test_phonebookCanSearch(self):
        self.assertEqual(1, self.test_phonebook.search_name('ZuZu'))
        self.assertEqual(1, self.test_phonebook.search_name('zuzu'))
        self.assertEqual(0, self.test_phonebook.search_name('Joe'))

    def test_phonebookCanRemove(self):
        len0 = len(self.contacts)
        len1 = len(self.test_phonebook.remove_contact('ZuZu'))
        self.assertEqual( len0, len1 + 1)
        self.assertEqual(0, self.test_phonebook.search_name('ZuZu'))


