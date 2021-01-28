from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        q = [root]
        while len(q) > 0:
            cur = q.pop()
            ans.append(cur.val)
            while cur.left is not None:
                if cur.right is not None:
                    q.append(cur.right)
                cur = cur.left
        return ans