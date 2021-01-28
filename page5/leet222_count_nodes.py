class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        cur = root
        layer = 1
        while cur.left is not None:
            cur = cur.left
            layer += 1
        left = 1 << (layer - 1)
        right = 1 << layer - 1
        while left <= right:
            middle = (left + right + 1) // 2
            if self.exist(root, middle, layer):
                left = middle
            else:
                right = middle
        return left

    def exist(self, root, n, l):
        for p in range(2, l + 1):
            right = (1 << (l - p)) & n
            if right:
                root = root.right
            else:
                root = root.left
        return root is not None