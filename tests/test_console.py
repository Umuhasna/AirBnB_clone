#!/usr/bin/python3
'''
Module
'''
import unittest
from unittest.mock import patch
from console import HBNBCommand
from io import StringIO


class TestConsole(unittest.TestCase):
    '''
    Docs
    '''
    def test_moduleDocs(self):
        '''
        Docs
        '''
        moduleDoc = __import__("console").__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_ClassDocs(self):
        '''
        Docs
        '''
        classDoc = __import__("console").HBNBCommand.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_ClassDocs(self):
        '''
        Docs
        '''

        functionDoc = __import__("console").HBNBCommand.__doc__
        self.assertGreater(len(classDoc), 0)



if __name__ == "__main__":
    unittest.main()
