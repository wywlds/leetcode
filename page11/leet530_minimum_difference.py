class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        max_difference = None
        last_value = None
        node = root
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            if last_value is None:
                last_value = node.val
            else:
                max_difference = min(max_difference, node.val - last_value) if max_difference is not None else \
                    (node.val - last_value)
                last_value = node.val
            node = node.right
        return max_difference

