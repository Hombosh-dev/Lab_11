"""Queue by Oleh Hombosh"""

class Node:
    """Represents base structure of node"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


class Queue:
    """Represent base Queue data-structure"""
    def __init__(self, head = None):
        if head:
            self.head = head
            current = head
            while current.next:
                current = current.next
            self.tail = current
        else:
            self.head = None
            self.tail = None

    def add(self, item):
        """Add elements to the tail of queue"""
        new_node = Node(item)
        if self.empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def deque(self):
        """Removes and returns the first element of queue"""
        if self.empty():
            return None
        dequeued = self.head
        self.head = self.head.next

        if self.head is None:
            self.tail = None
        return dequeued.data

    def peek(self):
        """Returns the first element from the queue without removing it"""
        if self.empty():
            return None
        return self.head.data

    def empty(self):
        """Checks if queue is empty"""
        return not bool(self.head)
