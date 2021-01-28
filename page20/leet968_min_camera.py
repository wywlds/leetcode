class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        def dfs(node):
            if node is None:
                return (1000, 0, 0)
            (a_l, b_l, c_l) = dfs(node.left)
            (a_r, b_r, c_r) = dfs(node.right)
            a = c_l + c_r + 1
            b = min(a, min(a_l + b_r, a_r + b_l))
            c = b_l + b_r
            return a, b, c
        return dfs(root)[1]