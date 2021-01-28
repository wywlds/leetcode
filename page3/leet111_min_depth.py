class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import sys
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root.left is None and root.right is None:
            return 1
        left_depth = self.minDepth(root.left) if root.left is not None else sys.maxsize
        right_depth = self.minDepth(root.right) if root.right is not None else sys.maxsize
        return min(left_depth, right_depth) + 1