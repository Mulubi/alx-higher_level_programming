#!/usr/bin/python3
"""Class that contains the base module"""
from models.base import Base


class Rectangle(Base):
    """Represents a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """INitializes a new Rectangle
        
        Args:
            width (int): THe width of the new rectangle.
            height (int): The height of the new rectangle.
            x (int): The x coordinate of the new rectangle.
            y (int): The y coordinate of the new rectangle.
            id (int): The identity of the new rectangle.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y <= 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """Set/get the width of the rectangle"""
            return self.__width

        @width.setter
        def width(self, value):
            if type(value) != int:
                raise TypeError("Width should be an integer!")
            if value <= 0:
                raise ValueError("Width must be a positive number!")
            self.__width = value

        @property
        def height(self):
            """Set/get the height of the rectangle"""
            return self.__height

        @height.setter
        def height(self, value):
            if type(value) != int:
                raise TypeError("Height should be an integer!")
            if value <= 0:
                raise ValueError("Height must be a positive number!")
            self.__height = value

        @property
        def x(self):
            """Set/get the x coordinate of the rectangle"""
            return self.__x

        @x.setter
        def x(self, value):
            if type(value) != int:
                raise TypeError("x coordinate should be an integer!")
            if value <= 0:
                raise ValueError("x coordinate must be a positive number!")
            self.__x = value

        @property
        def y(self):
            """Set/get the y coordinate of the rectangle"""
            return self.__y

        @y.setter
        def y(self, value):
            if type(value) != int:
                raise TypeError("y coordinate should be an integer!")
            if value <= 0:
                raise ValueError("y coordinate must be a positive number!")
            self.__y = value