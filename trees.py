"""
@Sebastian Urbina
A tree is a hierarchical data structure where each node has a value and could have 
one or more child nodes
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# Binary tree
root = Node(1)
root.left = Node(3)
root.right = Node(5)
root.left.left = Node(2)
root.left.right = Node(5)