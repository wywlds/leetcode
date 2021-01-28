

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        if root is None:
            return root
        q = collections.deque()
        q.append((1,root))
        while q:
            layer, node = q.popleft()
            if layer == d - 1:
                tmp_left = node.left
                tmp_right = node.right
                node.left = TreeNode(v)
                node.right = TreeNode(v)
                node.left.left = tmp_left
                node.right.right = tmp_right
            else:
                if node.left is not None:
                    q.append((layer + 1, node.left))
                if node.right is not None:
                    q.append((layer + 1, node.right))
        return root
