"""Counter node create by Hombosh Oleh"""
from node import Node

class CounterNode(Node):
    """Node with element counter"""
    def __init__(self, data):
        super().__init__(data)
        self.count = 1
