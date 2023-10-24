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
        return (self.__data)

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
        return (self.__next_node)

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

class SinglyLinkedList:
    """Define a singly linked list."""

    def __init__(self):
        """Constructor."""
        self.__head = None

    def __str__(self):
        """Print the singly linked list."""
        string = ""
        node = self.__head
        while node:
            string += str(node.data)
            if node.next_node:
                string += "\n"
            node = node.next_node
        return (string)

    def sorted_insert(self, value):
        """Insert a new Node into the correct sorted position in the list.

        Args:
            value (int): Value of the new node.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
            return
        if value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        node = self.__head
        while node.next_node and value > node.next_node.data:
            node = node.next_node
        new_node.next_node = node.next_node
        node.next_node = new_node