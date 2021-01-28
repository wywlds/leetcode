from typing import List

import copy
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root is None:
            return []
        self.ans = []
        self.dfs(root, [])
        return self.ans

    def dfs(self, root, base_path):
        base_path.append(root.val)
        if root.left is None and root.right is None:
            self.ans.append(copy.deepcopy(base_path))
        if root.left is not None:
            self.dfs(root.left)
        if root.right is not None:
            self.dfs(root.right)
        base_path.pop()