"""
Problem: Implement Stack using Queue
Solved by: Oleh Hombosh
"""
from my_queue import Queue

class MyStack(object):
    def __init__(self):
        self.que = Queue()
        self.count = 0

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.que.add(x)
        for _ in range(self.count):
            self.que.add(self.que.deque())
        self.count += 1

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        self.count -= 1
        return self.que.deque()

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.que.peek()

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return self.count == 0

        

obj = MyStack()
obj.push(4)
param_2 = obj.pop()
param_3 = obj.top()
param_4 = obj.empty()
print(param_2)
print(param_3)
print(param_4)
