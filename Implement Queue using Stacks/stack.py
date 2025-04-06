"""Stack by Oleh Hombosh"""

class Node:
    """Represents base structure of node"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Stack:
    """Represents stack"""
    def __init__(self, head = None):
        self.head = head

    def push(self, item):
        """Push element at the top of stack"""
        item = Node(item)
        if not self.head:
            self.head = item
            return
        item.next = self.head
        self.head = item

    def pop(self):
        """Pop element from the top of stack"""
        if self.head:
            item = self.head
            self.head = self.head.next
            return item.data
        return None

    def peek(self):
        """Returns element from the top of stack if exists, else None"""
        if self.head:
            return self.head.data
        return None

    def empty(self):
        """Check if stack is empty. Returns True if empty."""
        return not bool(self.head)
