#!/usr/bin/python3
'''
Module Docs:
'''
from datetime import datetime
import uuid


class BaseModel:
    '''
    Class Docs
    '''

    def __init__(self):
        '''
        Docs
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def save(self):
        '''
        Docs
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        Docs
        '''
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = type(self).__name__
        dictionary["created_at"] = self.created_at.isoformat()
        dictionary["updated_at"] = self.updated_at.isoformat()

        return dictionary

    def __str__(self):
        '''
        Docs
        '''
        class_name = type(self).__name__

        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
