#!/usr/bin/python3
class Base:
    """Base Model.
    
    This represents the base for all the other classes in this project
    
    Private Class Attributes:
    __nb_objects (Int) only available in this Base Model"""

    __nb_objects = 0
    def __init__(self, id=None):
        self.name = name
        self.id = id
        self.__nb_objects = nb_objects

    if id is not None:
        self.id = None
    else:
        __nb_objects += 1
        self.id = __nb_objects
