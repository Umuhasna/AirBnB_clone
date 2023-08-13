#!/usr/bin/python3
'''
Module Docs:
'''
from datetime import datetime
import uuid
import models


class BaseModel:
    '''
    Class Docs
    '''

    def __init__(self, *args, **kwargs):
        '''
        Docs
        '''
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.fromisoformat(value)
                    self.created_at = value
                elif key == 'updated_at':
                    value = datetime.fromisoformat(value)
                    self.updated_at = value
                elif key == 'id':
                    self.id = str(value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        '''
        Docs
        '''
        self.updated_at = datetime.now()
        models.storage.save()

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
