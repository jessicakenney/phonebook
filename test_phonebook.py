#!/usr/bin/python3.6

from contact import Contact
import unittest

class TestContact(unittest.TestCase):
    def setUp(self):
        pass

    def test_newContact(self):
        test_duck= Contact(feathers='green')
        self.assertEqual(True, type(test_duck) is Duck)
        self.assertEqual('green', test_duck.get_variable('feathers'))

    def test_duckCanQuack(self):
        test_duck= Contact(feathers='green')
        self.assertEqual('Quaaack!', test_duck.quack())





if __name__ == "__main__": unittest.main()
