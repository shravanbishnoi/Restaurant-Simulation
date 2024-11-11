"""
In this Module, A new Abstract Data Type called Postional List
is implemented

Author: Shravan
Date: 17-09-2023
"""
from Doubly_base import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """
    A sequential container of elements allowing positional access.
    """

    #-------------------------- nested Position class --------------------------

    class Position(object):
        """
        An abstraction representing the location of a single element.
        """

        def __init__(self, container, node):
            self._container = container
            self._node = node

        def element(self):
            """Returns the element stored at this position"""
            return self._node._element
        
        def __eq__(self, other):
            """Return True if other is a Position representing the same location."""
            return type(self) is type(other) and self._node is other._node
        
        def __ne__(self, other):
            """Return True if other does not represent the same location"""
            return not(self==other)
    
    #------------------------------- utility method -------------------------------

    def _validate(self, p):
        """Return position's node, or raise appropriate error if invalid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p._container is not self:
            raise  ValueError("p does not belong to this container")
        if p._node._next is None:
            raise ValueError("p is no longer valid")
        return p._node
    
    def _make_position(self, node):
        """Returns the position of the given node(Node for sentinels)"""
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)
    
    #------------------------------- accessors ------------------------------

    def first(self):
        """Return the first Position in the list (or None if list is empty)."""
        return self._make_position(self._header._next)
    
    def last(self):
        """Return the last Position in the list (or None if list is empty)."""
        return self._make_position(self._trailer._prev)
    
    def before(self, p):
        """Return the Position just before Position p (or None if p is first)."""
        node_at_p = self._validate(p)
        return self._make_position(node_at_p._prev)
    
    def after(self, p):
        """”Return the Position just after Position p (or None if p is last)."""
        node_at_p = self._validate(p)
        return self._make_position(node_at_p._next)

    def __iter__(self):
        """Generate a forward iteration of the elements of the list."""
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    #------------------------------- mutators -------------------------------

    # override inherited version to return Position, rather than Node
    def _insert_between(self, e, predecessor, successor):
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)
    
    def add_first(self, e):
        """Insert element e at the front of the list and return new Position."""
        return self._insert_between(e, self._header, self._header._next)
    
    def add_last(self, e):
        """Insert element e at the end of the list and return new Position."""
        return self._insert_between(e, self._trailer._prev, self._trailer)
    
    def add_before(self, p, e):
        """Insert element e into list before Position p and return new Position."""
        node = self._validate(p)
        return self._insert_between(e, node._prev, node)
    
    def add_after(self, p, e):
        """Insert element e into list after Position p and return new Position."""
        node = self._validate(p)
        return self._insert_between(e, node, node._next)
    
    def delete(self, p):
        """Remove and return the element at Position p."""
        return super()._delete_node(self._validate(p))
    
    def replace(self, p, e):
        """Replace the element at Position p with e.

        Return the element formerly at Position p."""
        node = self._validate(p)
        element_node = node._element
        node._element = e
        return element_node