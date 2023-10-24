#!/usr/bin/python3

class Square:
    """Define a square."""
    
    def __init__(self, size=0):
        """Constructor.
        
        Args:
            size (int): The size of the new square.
        """
        self.size = size
        
    @property
    def size(self):
        """Return the size of the square."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Set the size of the square.
        
        Args:
            value (int): The new size of the square.
            
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must br >= 0")
        self.__size = value
    
    def area(self):
        """Return the area of the square."""
        return self.__size ** 2
    
    def __eq__(self, other):
        """Check if two squares are equal."""
        return self.area() == other.area()
    
    def __ne__(self, other):
        """Check if two squares are not equal."""
        return self.area() != other.area()
    
    def __lt__(self, other):
        """Check if a square is less than another square."""
        return self.area() < other.area()
    
    def __le__(self, other):
        """Check if a square is less than or equal to another square."""
        return self.area() <= other.area()
    
    def __gt__(self, other):
        """Check if a square is greater than another square."""
        return self.area() > other.area()
    
    def __ge__(self, other):
        """Check if a square is greater than or equal to another square."""
        return self.area() >= other.area()
