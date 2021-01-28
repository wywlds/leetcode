class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root is None:
            return 0
        ans = 0
        def visit(node):
            nonlocal ans
            if node.left is None and node.right is None:
                ans += node.val
            if node.left is not None:
                node.left.val = node.val * 10 + node.left.val
                visit(node.left)
            if node.right is not None:
                node.right.val = node.val * 10 + node.right.val
                visit(node.right)
        visit(root)
        return ans