#!/usr/bin/python3
'''
Module Docs:
'''
from models.base_model import BaseModel


class User(BaseModel):
    '''
    Class Docs
    '''

    email = ""
    password = ""
    first_name = ""
    last_name = ""
