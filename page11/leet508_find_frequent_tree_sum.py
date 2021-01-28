from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        self.count_dict = {}
        self.check_tree_node_sum(root)
        max_count = max(self.count_dict.values())
        result = []
        for k, v in self.count_dict.items():
            if v == max_count:
                result.append(k)
        return result

    def check_tree_node_sum(self, node):
        if node.left is not None:
            left_sum = self.check_tree_node_sum(node.left)
        else:
            left_sum = 0
        if node.right is not None:
            right_sum = self.check_tree_node_sum(node.right)
        else:
            right_sum = 0
        sum = left_sum + right_sum + node.val
        if sum in self.count_dict:
            self.count_dict[sum] += 1
        else:
            self.count_dict[sum] = 1
        return sum