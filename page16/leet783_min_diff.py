class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        last = float("-inf")
        min_diff = float("inf")
        def visit(num):
            nonlocal last, min_diff
            diff = num - last
            min_diff = min(diff, min_diff)
            last = num
        def visit_node(node):
            if root.left is not None:
                visit_node(root.left)
            visit(node.val)
            if root.right is not None:
                visit_node(root.right)
        return min_diff
