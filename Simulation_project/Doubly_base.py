"""
This module contains the base class of Doubly Linked Lists

Author: Shravan
Date: 17-09-2023
"""

class _DoublyLinkedBase(object):
    """
    A base class providing a Doubly Linked List representation
    """

    #-------------------------- nested Node class --------------------------

    class _Node(object):
        """
        Lightweight, nonpublic class representing a doubly linked list node
        """
        __slots__ = '_element', '_prev', '_next'
        def __init__(self, element, prev, next):
            """Initialises a Node for Doubly Linked List"""
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        """Initialises a Doubly Linked List object"""
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    def __len__(self):
        """Length operator overloading"""
        return self._size
    
    def is_empty(self):
        """Returns True if size is 0 else False"""
        return len(self)==0
    
    def _insert_between(self, e, predecessor, successor):
        """Adds e between the predecessor and successor"""
        
        new_node = self._Node(e, predecessor, successor)
        predecessor._next = new_node
        successor._prev = new_node
        self._size += 1
        return new_node

    def _delete_node(self, node):
        """Returns and deletes nonsentinel node from the list"""
        node_value = node._element
        previous_node = node._prev
        next_node = node._next
        previous_node._next = next_node
        next_node._prev = previous_node
        node._element = node._prev =  node._next = None  # deprecate node
        self._size -= 1
        return node_value


    # ### Practice Problem Q.3 Solution
    # ### Q.3 Write a program to delete a node in DLL (Doubly Linked List) containing the value entered by the user
    # def delete_node(self, value):
    #     """Deletes the node with the given value"""
    #     node = self._header._next
    #     return_value = node._element
    #     while node._element!=value or node._next==None:
    #         node = node._next
    #     predecessor = node._prev
    #     successor = node._next
    #     predecessor._next = successor
    #     successor._prev = predecessor
    #     node._element = node._prev =  node._next = None  # deprecate node
    #     self._size -= 1
    #     return return_value


    # ### Practice Problem Q.3 Solution
    # ### Q.4 Write a program to count the number of nodes in a circularly linked list.
    # def count_nodes(self):
    #     """Returns the number of nodes present in the DLL"""
    #     count = 0
    #     node = self._header._next
    #     while node!= self._trailer:
    #         count += 1
    #         node = node._next
    #     return count