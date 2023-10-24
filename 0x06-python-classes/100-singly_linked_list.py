#!/usr/bin/python3

class Node:
    """Define a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Constructor.

        Args:
            data (int): Data stored in the node.
            next_node (Node): Next node in the singly linked list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Return data stored in the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data stored in the node.

        Args:
            value (int): Data stored in the node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Return next node in the singly linked list."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next node in the singly linked list.

        Args:
            value (Node): Next node in the singly linked list.

        Raises:
            TypeError: If value is not a Node object.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value