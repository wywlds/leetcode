class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.diameter = 0
        self.get_height(root)

    def get_height(self, node):
        if node == None:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        height = max(left_height, right_height) + 1
        sub_diameter = left_height + right_height
        self.diameter = max(self.diameter, sub_diameter)
        return height
