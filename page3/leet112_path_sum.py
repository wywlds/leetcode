class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root.left is None and root.right is None:
            return root.val == sum
        if root.left is not None and self.hasPathSum(root.left, sum - root.val):
            return True
        if root.right is not None and self.hasPathSum(root.right, sum - root.val):
            return True
        return False