class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return

        def flatten_internal(node: TreeNode):
            left_node = node.left
            right_node = node.right
            left = right = node
            if left_node:
                left_start_node, left_end_node = flatten_internal(left_node)
                right.left = None
                right.right = left_start_node
                right = left_end_node
            if right_node:
                right_start_node, right_end_node = flatten_internal(right_node)
                right.left = None
                right.right = right_start_node
                right = right_end_node
            return left, right
        flatten_internal(root)