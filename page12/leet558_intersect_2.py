"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

from collections import deque
class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        print(quadTree1)
        print(quadTree2)