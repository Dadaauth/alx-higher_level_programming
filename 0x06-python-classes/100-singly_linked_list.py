#!/usr/bin/python3
"""
a module for creating a singly linked list data structure
"""


class Node:
    """
    A class for each node in the structure
    """
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if next_node is not None and not isinstance(next_node, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    a class to manipulate the linked list
        Capabilities:
            + insert into the linked list
            + represent the linked list in a string format when printed
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new = Node(value, None)
        if self.__head is None:
            self.__head = new
        else:
            tmp = self.__head
            if value < tmp.data:
                new.next_node = tmp
                self.__head = new
            else:
                while tmp.next_node is not None:
                    if value < tmp.next_node.data:
                        break
                    tmp = tmp.next_node
                new.next_node = tmp.next_node
                tmp.next_node = new

    def __repr__(self):
        tmp = self.__head
        val_str = ""
        while tmp is not None:
            val_str += f"{tmp.data}\n"
            tmp = tmp.next_node
        val_str = val_str[:-1]
        return val_str
