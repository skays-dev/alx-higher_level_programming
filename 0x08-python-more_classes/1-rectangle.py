#!/usr/bin/python3
"""Defining an empty class Rectangle"""

class Rectangle:
    """Representation of a Rectangle"""
    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width
        
    @property
    def width(self):
        """getter method for width"""
        return self.__width
    
    @width.setter
    def width(self, value):
        """setter method for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0 :
            raise ValueError("width must be >= 0")
        self.__width = value
        
    @property
    def height(self):
        """getter method for height"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """setter method for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0 :
            raise ValueError("height must be >= 0")
        self.__height = value
