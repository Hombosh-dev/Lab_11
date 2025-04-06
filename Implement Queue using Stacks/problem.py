"""
Problem: Implement Queue using Stacks
Solved by: Oleh Hombosh
"""
from stack import Stack

class MyQueue(object):
    """Represent Queue, which works by 2 stacks"""
    def __init__(self):
        self.stack_1 = Stack()
        self.stack_2 = Stack()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_1.push(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.stack_2.empty():
            while not self.stack_1.empty():
                self.stack_2.push(self.stack_1.pop())
        return self.stack_2.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.stack_2.empty():
            while not self.stack_1.empty():
                self.stack_2.push(self.stack_1.pop())
        return self.stack_2.peek()

    def empty(self):
        """
        :rtype: bool
        """
        return self.stack_2.empty() and self.stack_1.empty()

if __name__ == "__main__":
    output_list = []
    myQueue = MyQueue()
    output_list.append(myQueue.push(1))
    output_list.append(myQueue.push(2))
    output_list.append(myQueue.peek())
    output_list.append(myQueue.pop())
    output_list.append(myQueue.empty())
    assert output_list == [None, None, 1, 1, False]
    print("Base test passed!")
