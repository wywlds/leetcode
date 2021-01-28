from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        def dfs(node, base_list, base_sum):
            if node.left is None and node.right is None:
                if node.val + base_sum == sum:
                    base_list.append(node.val)
                    ans.append(base_list[:])
                    base_list.pop()
            else:
                base_sum += node.val
                base_list.append(node.val)
                if node.left is not None:
                    dfs(node.left, base_list, base_sum)
                if node.right is not None:
                    dfs(node.right, base_list, base_sum)
                base_list.pop()
        dfs(root, [], 0)
        return ans