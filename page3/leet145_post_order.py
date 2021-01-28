from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        q =[]
        ans = []
        q.append(root)
        while q:
            node = q.pop()
            ans.append(node.val)
            if node.right is not None:
                q.append(node.right)
            if node.left is not None:
                q.append(node.left)
        return ans[::-1]
