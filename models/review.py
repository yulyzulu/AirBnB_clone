#!/usr/bin/python3
'''
Module to execute the functions
'''

from models.base_model import BaseModel


class Review(BaseModel):
    ''' Review Class '''

    place_id = ""  # string - empty string: it will be the Place.id
    user_id = ""  # string - empty string: it will be the User.id
    text = ""  # string - empty string
