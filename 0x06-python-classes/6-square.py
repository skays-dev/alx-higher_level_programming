#!/usr/bin/python3
"""Square module."""


class Square:
    """Define a square"""

    def __init__(self, size=0, position=(0, 0)):
        """Constructor.

        Args:
            size: Length of a side of the square.
            position (int, int) : The position of the new square.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set position of the square.

        Args:
            value (int, int): New position of the square.

        Raises:
            TypeError: If position is not a tuple of 2 positive integers.
        """
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0], end="")
            print('#' * self.__size)
