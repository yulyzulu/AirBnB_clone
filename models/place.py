#!/usr/bin/python3
'''
Module to execute the functions
'''

from models.base_model import BaseModel


class Place(BaseModel):

    ''' Place Class '''
    city_id = ""  # string - empty string: it will be the City.id
    user_id = ""  # string - empty string: it will be the User.id
    name = ""  # string - empty string
    description = ""  # string - empty string
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []  # list of string - empty list
