#!/usr/bin/python3
"""
This module contains the definition for two classes, the Node class and the
SinglyLinkedList class.

Node:
    This class contains two private instance variable.
 
    data (int): Holds the integer value for the node
    next_node (Node): The pointer to the next Node

    Getters and Setter for the both variables are defined in the class

SinglyLinkedList:
    This class creates a singly linked list using the 'Node' class as nodes for
    the list. There is only one private instance variable defined in this class

    head (Node): A Pointer to the head of the linked list

    It also defines a function 'sorted_insert' which inserts nodes to the list
    in ascending order. This class also override the built-in '__str__'
    function to print each node in the list in a new line
"""


class Node:
    """A Node class, like a node in a SinglyLinkedList has two member variables

    The __init__ method like other constructors initializes the value of the
    member variables data and next_node to the ones passed in the argument, it
    also performs some safety checks to ensure the right data type is passed

    Args:
        data (int): The integer value(data) that the current node holds
        next_node (Node): A pointer to the next_node
    """
    def __init__(self, data, next_node=None):
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        if not isinstance(next_node, Node) and next_node is not None:
            raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        A getter method to retrieve the value of the private instance variable
        data
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """
        Sets the value of the private instance variable data to value.
        Also carry out a type check to ensure value is an integer type

        Args:
            value (int): Value to set data to
        """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """
        Returns the member variable next_node which points to the next node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """
        A setter method to the private instance variable next_node which points
        to the next node

        Args:
            value (Node): Value to assign to the next_node member variable
        """
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """This class utilizes the Node class to make a singly linked list.
    There is a sorted_insert function that inserts node such a way that the
    linked list is sorted in ascending order.

    Args:
        head (Node): A pointer to the head of the singly linked list
    """
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """
        This method inserts a new Node into the correct sorted position in the
        list (increasing order)

        Args:
            value (int): Data value to assign to the new node
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        if self.__head is None:
            self.__head = Node(value)
        else:
            itr = self.__head
            prev = None
            while (itr is not None):
                if value < itr.data:
                    new = Node(value, itr)
                    if prev is not None:
                        prev.next_node = new
                    else:
                        self.__head = new
                    break
                elif value == itr.data:
                    nxt = itr.next_node
                    new = Node(value, nxt)
                    itr.next_node = new
                    break
                elif value > itr.data:
                    if itr.next_node is None:
                        itr.next_node = Node(value)
                        break
                prev = itr
                itr = itr.next_node

    def __str__(self):
        """Overrides the built-in function __str__ which displays the string
        representation so that each 'Node' in the singly linked list is printed
        in a new line
        """
        itr = self.__head
        ret = ""
        first = True
        while itr is not None:
            if not first:
                ret += '\n'
            ret += str(itr.data)
            first = False
            itr = itr.next_node
        return (ret)
