#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square"""

    def __init__(self, size=0):
        """Constructor.

        Args:
            size: Length of a side of the square.
        """
        self.__size = size

    @property
    def size(self):
        """Return size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set size of the square.

        Args:
            value: New size of the square.

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
        """Return area of the square."""
        return self.__size**2
    
    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__size):
            print('#' * self.__size)
