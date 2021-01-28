class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if self.isEqual(s, t):
            return True
        if s is None:
            return False
        if self.isSubtree(s.left, t) or self.isSubtree(s.right, t):
            return True
        return False

    def isEqual(self, s:TreeNode, t:TreeNode) -> bool:
        if s is None and t is None:
            return True
        if s is None or t is None:
            return False
        if s.val == t.val:
            return self.isEqual(s.left, t.left) and self.isEqual(s.right, t.right)
        else:
            return False