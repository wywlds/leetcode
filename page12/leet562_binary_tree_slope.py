# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.sum = 0
        self.get_sum(root)
        return self.sum

    def get_sum(self, root):
        if root is None:
            return 0
        left_sum = self.get_sum(root.left)
        right_sum = self.get_sum(root.right)
        self.sum = abs(left_sum - right_sum)
        return left_sum + right_sum + root.val