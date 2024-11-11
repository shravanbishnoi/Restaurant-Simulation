from Doubly_base import _DoublyLinkedBase
from queue_exception import Empty

class Dll_Deque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list."""

    def __iter__(self):
        current = self._header._next
        while current is not self._trailer:
            yield current._element
            current = current._next

    def first(self):
        """Returns the first element(just after the header) from the Deque/DLL"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element
    
    def last(self):
        """Returns the last element(element just before the trailer) from the Deque/DLL"""
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._prev._element
    
    def insert_first(self, e):
        """Inserts the element e as a first element of Deque"""
        self._insert_between(e, self._header, self._header._next)

    def insert_last(self, e):
        """Inserts the element e at last of the Deque"""
        self._insert_between(e, self._trailer._prev, self._trailer)

    def delete_first(self):
        """Returns and deletes first element of the Deque
        
        Raise Exception if the Deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)
    
    def delete_last(self):
        """Returns and deletes last element of the Deque
        
        Raise Exception if the Deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._prev)
    
    def concatenate(self, other_deque):
        """Attaches another deque after the current deque."""
        if isinstance(other_deque, Dll_Deque):
            if not other_deque.is_empty():
                self._trailer._prev._next = other_deque._header._next
                other_deque._header._next._prev = self._trailer._prev
                self._trailer = other_deque._trailer
                self._size += len(other_deque)
                other_deque._header._next = other_deque._trailer = None
                other_deque._size = 0
            else:
                raise Empty("The other deque is empty")
        else:
            raise ValueError("The argument is not a valid deque.")
