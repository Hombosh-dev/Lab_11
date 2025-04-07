"""Node created Hombosh Oleh"""


class Node:
    """Represents base structure of node"""
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)
