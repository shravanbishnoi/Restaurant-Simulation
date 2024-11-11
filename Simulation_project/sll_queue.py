'''
This is a module containing Queue class
In this module a Singly Linked List based queue is implemented

Author: Shravan
Date: 11-09-2023
'''
from queue_exception import Empty

####-----------------------------------Array based queue----------------------------####
class Sll_queue(object):
    """
	FIFO queue implementation using Singly Linked List as an underlying storage
	"""

    class _Node(object):
        """
        This class represents a light weight object which is building block for a SLL/Queue
        """
        __slots__ = '_element', '_next'
        def __init__(self, e=None, next=None):
            """
            Initializes a Node object
            """
            self._element = e
            self._next = next
    
    def __init__(self, item):
        """
        Initializes a SLL object/Queue
        """
        self._head = None
        self._tail = None
        self._size = 0              # Number of queue elements
        self._heapitem = item

    def __len__(self):
        """Returns the length of the Queue"""
        return self._size
    
    def is_empty(self):
        """Returns True if the Queue is empty otherwise False"""
        return self._size==0

    def first(self):
        """Returns(but do not removes) First element of the Queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._head._element
    def last(self):
        """Returns(but do not removes) Last element of the Queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        return self._tail._element

    def enqueue(self, e):
        """Adds element e to the Queue"""
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
           self._tail._next = newest
        self._tail = newest
        self._size += 1

    def dequeue(self):
        """Returns and removes first element of the Queue"""
        if self.is_empty():
            raise Empty("Queue is empty")
        value = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
             self._tail = None
        return value



# ###-----------------------Testing-----------------------------####

# if __name__ == '__main__':
# 	print("Testing started: ")
# 	obj = Sll_queue()
# 	print("Length at starting: ",len(obj))
# 	print("Is Empty: ", obj.is_empty())
# 	for i in range(50):
# 		obj.enqueue(i)
# 	print("Length after Enqueuing 50 elements: ",len(obj))
# 	print("Is Empty: ", obj.is_empty())
# 	print("First element: ", obj.first())
# 	for i in range(50):
# 		obj.dequeue()

# 	print("Testing completed")

            
