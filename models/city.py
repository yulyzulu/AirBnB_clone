#!/usr/bin/python3
'''
Module to execute the functions
'''

from models.base_model import BaseModel


class City(BaseModel):
    ''' City Class '''

    state_id = ""  # string - empty string: it will be the State.id
    name = ""  # string - empty string
