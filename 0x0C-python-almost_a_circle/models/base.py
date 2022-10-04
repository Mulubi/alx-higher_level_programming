#!/usr/bin/python3

"""Defines a base model class"""
class Base:
    """Base Model.
    
    This represents the base for all the other classes in this project
    
    Private Class Attributes:
    __nb_objects (Int): number of instantiated Bases
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base
        
        Args:
            id (int): The id of every new base
        """

        self.name = name
        self.id = id
    
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
