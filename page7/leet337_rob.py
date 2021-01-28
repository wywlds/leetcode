class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        inc, ex = self.rob_internal(root)
        return inc

    def rob_internal(self, root):
        if root is None:
            return 0, 0
        left_inc, left_ex = self.rob_internal(root.left)
        right_inc, right_ex = self.rob_internal(root.right)
        inc = max(left_ex + right_ex + root.val, left_inc + right_inc)
        ex = left_inc + right_inc
        return inc, ex


if __name__=="__main__":
    node1 = TreeNode(3)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(3)
    node5 = TreeNode(1)
    node1.left