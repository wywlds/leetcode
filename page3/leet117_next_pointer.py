"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


import collections
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        q = collections.deque()
        q.append((root, 0))
        if not root:
            return root
        while len(q) != 0:
            node, layer = q.popleft()

            if node.left is not None:
                q.append((node.left, layer + 1))
            if node.right is not None:
                q.append((node.right, layer + 1))

            if len(q) == 0:
                return root
            if q[0][1] == layer:
                node.next = q[0][0]
        return root



if __name__=="__main__":
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    solution = Solution()
    root = solution.connect(node1)
    pass