from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import collections
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if root is None:
            return []
        q = collections.deque()
        q.append((1, root))
        cur_layer = 1
        cur_sum = 0
        cur_count = 0
        result = []
        while q:
            layer, node = q.popleft()
            if layer == cur_layer:
                cur_sum += node.val
                cur_count += 1
            else:
                result.append(cur_sum/cur_count)
                cur_layer = layer
                cur_sum = node.val
                cur_count = 1
            if node.left is not None:
                q.append((layer + 1, node.left))
            if node.right is not None:
                q.append((layer + 1, node.right))
        result.append(cur_sum/cur_count)
        return result
