from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        depth = self.get_depth(root)
        matrix = [[""] * (2 ** depth - 1) for _ in range(depth)]
        self.assign(matrix, 0, 0, 2**depth - 2, root)
        return matrix

    def get_depth(self, root):
        if root is None:
            return 0
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        return max(left_depth, right_depth) + 1

    def assign(self, matrix, depth, left, right, root):
        if root is None:
            return
        mid = (left + right) //2
        matrix[depth][mid] = root.val
        self.assign(matrix, depth + 1, left, mid - 1, root.left)
        self.assign(matrix, depth + 1, mid + 1, right, root.right)