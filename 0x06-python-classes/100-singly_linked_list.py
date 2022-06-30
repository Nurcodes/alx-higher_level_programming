#!/usr/bin/python3
"""Class node of a singly linked list"""


class Node:
    """Define a node a class"""

    def __init__(self, data, next_node=None):
        """Instantiate a new node object

        Args:
            data (int): must be an integer
            next_node (Node): can be None or Node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        """To set the data attribute of the object

        Args:
            value (int): must be an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """To set the next node attribute of the object

        Args:
            value (Node or None): Value of next_node
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""SinglyLinkedList that defines a singly linked list"""


class SinglyLinkedList:
    """define singlylinked list"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)
        """ If the list is empty the new node becomes the head """
        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node

        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while(tmp.next_node is not None and tmp.next_node.data < value):
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        vals = []
        tmp = self.__head
        while tmp is not None:
            vals.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(vals))
