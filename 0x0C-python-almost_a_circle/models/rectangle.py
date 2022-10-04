#!/usr/bin/python3
import base
"""Class that contains the base module"""


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__()

        @property
        def width(self):
            return self.__width
        def height(self):
            return self.__height
        def x(self):
            return self.__x
        def y(self):
            return self.__y

        @width.setter
        def width(self):
            self.__width = width

        @height.setter
        def height(self):
            self.__height = height

        @x.setter
        def x(self):
            self.__x = x

        @y.setter
        def y(self):
            self.__y = y


        
