# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        ans = []
        def dfs(node):
            if node is None:
                return
            if node.left is not None:
                ans.append(node.left.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return sum(ans)