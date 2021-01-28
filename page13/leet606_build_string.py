class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if t.left is None and t.right is None:
            return str(t.val)
        left = "()" if t.left is None else "(" + self.tree2str(t.left) + ")"
        right = "" if t.right is None else "(" + self.tree2str(t.right) + ")"
        return "%d%s%s"%(t.val, left, right)