class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        q = collections.deque()
        q.append((0, 0, root))
        cur_depth = -1
        left = 0
        right = 0
        max_width = 0
        while q:
            depth, h_pos, node = q.popleft()
            if depth != cur_depth:
                max_width = max(right - left, max_width)
                cur_depth = depth
                right = h_pos
                left = h_pos
            else:
                right = h_pos
            if node.left is not None:
                q.append((depth + 1, 2 * h_pos, node.left))
            if node.right is not None:
                q.append((depth + 1, 2 * h_pos, node.right))
        max_width = max(right - left, max_width)
        return max_width