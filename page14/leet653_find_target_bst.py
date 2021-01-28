class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        needs = set()
        q = collections.deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node is None:
                continue
            if node.val in needs:
                return True
            else:
                needs.add(k - node.val)
            q.append(node.left)
            q.append(node.right)
        return False