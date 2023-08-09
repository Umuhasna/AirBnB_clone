#!/usr/bin/python3
'''
Module
'''
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime


def mock_uuid():
    '''
    Docs
    '''
    return UUID("b6a6e15c-c67d-4312-9a75-9d084935e579")

def mock_datetime():
    '''
    Docs
    '''
    return datetime(2017, 9, 28, 21, 5, 54, 119434)

class TestBaseModel(unittest.TestCase):
    '''
    Docs
    '''
    def test_moduleDocs(self):
        '''
        Docs
        '''
        moduleDoc = __import__("models.base_model").base_model.__doc__
        self.assertGreater(len(moduleDoc), 0)

    def test_classDocs(self):
        '''
        '''
        classDoc = __import__("models.base_model").base_model.BaseModel.__doc__
        self.assertGreater(len(classDoc), 0)

    def test_methodDocsSave(self):
        '''
        '''
        methodDoc = __import__("models.base_model").base_model.BaseModel.save.__doc__
        self.assertGreater(len(methodDoc), 0)

    def test_methodDocsto_dict(self):
        '''
        '''
        methodDoc = __import__("models.base_model").base_model.BaseModel.to_dict.__doc__
        self.assertGreater(len(methodDoc), 0)

    def test_methodDocs__str___(self):
        '''
        '''
        methodDoc = __import__("models.base_model").base_model.BaseModel.__str__.__doc__
        self.assertGreater(len(methodDoc), 0)

    def test_idType(self):
        '''
        '''
        obj = BaseModel()
        self.assertIs(obj.id, str)

    def test_idLength(self):
        '''
        '''
        obj = BaseModel()
        self.assertEqual(len(obj.id), 32)

    def test_idValidity(self):
        '''
        '''
        obj = BaseModel()
        value = UUID(obj.id)
        self.assertIs(value, UUID)

    def test_created_atType(self):
        '''
        '''
        obj = BaseModel()
        self.assertIs(obj.created_at, datetime)

    def test_updated_atType(self):
        '''
        '''
        obj = BaseModel()
        self.assertIs(obj.updated_at, datetime.datetime)

    @patch('datetime.now', mock_datetime)
    @patch('uuid.uuid4', mock_uuid)
    def test_outputOf__str__(self):
        '''
        '''
        obj = BaseModel()
        obj.name = "My First Model"
        obj.my_number = 89

        string1 = obj.__str__
        string2 = "[BaseModel] (b6a6e15c-c67d-4312-9a75-9d084935e579) {'my_number': 89, 'name': 'My First Model', 'updated_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434), 'id': 'b6a6e15c-c67d-4312-9a75-9d084935e579', 'created_at': datetime.datetime(2017, 9, 28, 21, 5, 54, 119434)}"

        self.assertEqual(string1, string2)

    def test_updated_atChanged(self):
        '''
        '''
        obj = BaseModel()
        time1 = obj.updated_at
        obj.id = uuid.uuid4()
        self.assertGreater(obj.updated_at, time1)

    def test_to_dictCheck(self):
        '''
        '''
        obj = BaseModel()
        to_dict_dict = obj.to_dict()
        __dict__dict = obj.__dict__

        for keys in __dict__dict:
            self.assertIn(keys, to_dict_dict)
            self.assertEqual(__dict__dict[keys], to_dict_dict[keys])

    def test_to_dict(self):
        '''
        '''
        obj = BaseModel()
        to_dict_dict = obj.to_dict()

        self.assertIn("__class__", to_dict_dict)
        self.assertIs(to_dict_dict["__class__"], str)

    @patch('datetime.now', mock_datetime)
    def test_to_dict_Valid(self):
        '''
        '''
        value = "2017-09-28T21:05:54.119434"
        obj = BaseModel()
        to_dict_dict = obj.to_dict()

        self.assertIn("created_at", to_dict_dict)
        self.assertIn("updated_at", to_dict_dict)
        self.assertIs(to_dict_dict["created_at"], str)
        self.assertIs(to_dict_dict["updated_at"], str)
        self.assertEqual(to_dict_dict["created_at"], value)
        self.assertEqual(to_dict_dict["updated_at"], value)

    def test_dictType(self):
        '''
        '''
        obj = BaseModel()
        to_dict_dict = obj.to_dict()

        self.assertIs(to_dict_dict["id"], str)
