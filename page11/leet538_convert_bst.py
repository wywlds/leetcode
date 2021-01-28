class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        stack = []
        node = root
        agg = 0
        while stack or node:
            while node:
                stack.append(node)
                node = node.right
            node = stack.pop()
            agg += node.val
            node.val = agg
            node = node.left
        return root