# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        lowest = root
        if p.val > q.val:
            p, q = q, p
        def dfs(node):
            if node.val > q.val:
                dfs(node.left)
            elif node.val < p.val:
                dfs(node.right)
            else:
                lowest = node
        return lowest