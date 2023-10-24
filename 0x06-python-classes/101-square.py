#!/usr/bin/python3


class Square:
    """Define a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.

        Raises:
            TypeError: If size or position are not integers.
            ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """Return the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square.

        Args:
            value (int, int): The new position of the square.

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
        """Return the area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square."""
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for i in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Return the string representation of the square."""
        string = ""
        if self.__size == 0:
            return string
        for i in range(self.__position[1]):
            string += "\n"
        for i in range(self.__size):
            string += " " * self.__position[0] + "#" * self.__size + "\n"
        return string[:-1]
