"""
Problem: Maximum Frequency Stack
Solved by: Oleh Hombosh
"""
from counter_node import CounterNode

class FreqStack(object):
    """Represent frequency stack whichi solves problem from leetcode"""
    def __init__(self):
        self.head = None

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        new_node = CounterNode(val)
        new_node.count += self.count_value_frequency(val)
        new_node.next = self.head
        self.head = new_node

    def count_value_frequency(self, val):
        """Counts how many times value repeats in stack"""
        curr = self.head
        while curr:
            if curr.data == val:
                return curr.count
            curr = curr.next
        return 0

    def pop(self):
        """
        :rtype: int
        """
        max_frequency_count = -1
        max_frequency_address = None
        curr = self.head
        while curr:
            if curr.count > max_frequency_count:
                max_frequency_count = curr.count
                max_frequency_address = curr
            curr = curr.next

        self.remove_element(max_frequency_address)
        return max_frequency_address.data

    def remove_element(self, address):
        """Removes node by address (node object) from stack"""
        if self.head is None:
            return

        if self.head is address:
            self.head = self.head.next
            return

        current = self.head
        while current.next is not None:
            if current.next is address:
                current.next = current.next.next
                return
            current = current.next

    def __str__(self):
        curr = self.head
        _str = ""
        while curr:
            _str += f"{curr.data} -> "
            curr = curr.next
        return _str.strip(' -> ')
