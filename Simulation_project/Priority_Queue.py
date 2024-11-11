"""
In this Module, A new Abstract Data Type called Priority Queue
is implemented using unsorted list, sorted list and heap.

Author: Shravan
Date: 19-10-2023
"""
from queue_exception import Empty
from positional_list import PositionalList

class PriorityQueueBase(object):
    """An Abstract base class for priority queue."""

    class _Item():
        """Lightweight composite to store priority queue items."""
        __slot__ = '_key', '_value', '_index'

        def __init__(self, k, v, i):
            self._key = k
            self._value = v
            self._index = i # is the index in the heap

        def __lt__(self, other):
            return self._key < other._key
        
        def __eq__(self, other):
            return self._key == other._key
        
        def update_key(self, incr):
            self._key = self._key + incr
    
    def is_empty(self):
        """Return True if the priority queue is empty otherwise false."""
        return len(self) == 0


###----------------------------Implementation Using sorted list---------------------###

class HeapPriorityQueue(PriorityQueueBase):
    """A min-oriented priority queue implemented with a binary heap."""

    ##------------------------------ nonpublic behaviors -----------------------------##
    def _parent(self, j):
        return (j-1)//2
    
    def _left(self, j):
        return 2*j + 1
    
    def _right(self, j):
        return 2*j + 2
    
    def _has_left(self, j):
        return self._left(j) < len(self._data)
    
    def _has_right(self, j):
        return self._right(j) < len(self._data)
    
    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]
        self._data[i]._index, self._data[j]._index = self._data[j]._index, self._data[i]._index

    def _upheap(self, j):
        parent = self._parent(j)
        if j>0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)           # Recursion
        elif j>0 and self._data[j] == self._data[parent] and self._data[j]._value < self._data[parent]._value:
            self._swap(j, parent)
            self._upheap(parent)

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)     # Recursion
            elif self._data[small_child] == self._data[j] and self._data[small_child]._value < self._data[j]._value:
                self._swap(j, small_child)
                self._downheap(small_child)

    ##------------------------------ public behaviors --------------------------------##
    def __init__(self, k):
        """Create a new empty Priority Queue."""
        self._data = []
        for i in range(k):
            self._data.append(self._Item(0, i, i))

    def __len__(self):
        """Return the number of items in the Priority Queue."""
        return len(self._data)
    
    def getIndex(self, item):
        """Returns the index of the item"""
        return item._index
    
    def add(self, key, value, idx):
        """Add a key-value pair to the priority queue."""
        self._data.append(self._Item(key, value, idx))
        self._upheap(len(self._data)-1)

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key.
    
        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty("Priority Queue is empty.")
        item = self._data[0]
        return (item._key, item._value)
    
    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key.
        
        Raise Empty exception if empty."""
        if self.is_empty():
            raise Empty("Priority Queue is empty.")
        self._swap(0, len(self._data)-1)                  
        item = self._data.pop()                           # put minimum item at the end
        self._downheap(0)                                 # and remove it from the list;
        return (item._key, item._value)                   # then fix new root
    
    def update_rootkey(self, incr):
        """Updates the root's key to new key"""
        if self.is_empty():
            raise Empty("Priority Queue is empty.")
        self._data[0].update_key(incr)
        self._downheap(0)

    def update(self, idx, incr):
        self._data[idx].update_key(incr)
        self._upheap(idx)

    def __iter__(self):
        for i in self._data:
            yield i
