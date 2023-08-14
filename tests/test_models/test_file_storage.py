#!/usr/bin/python3
'''
Module
'''
import unittest
from models.file_storage import FileStorage
from uuid import UUID
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    '''
    Docs
    '''
    def test_moduleDocs(self):
        '''
        Docs
        '''
        moduleDoc = __import__("models.file_storage").file_storage.__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        Docs
        '''
        classDoc = __import__("models.file_storage").file_storage.FileStorage.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_methodDocsSave(self):
        '''
        Docs
        '''
        methodDoc = (
                __import__("models.file_storage")
                .file_storage.FileStorage.save.__doc__)
        self.assertGreater(len(methodDoc), 0)

if __name__ == "__main__":
    unittest.main()
