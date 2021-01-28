from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        len_N = len(nums)
        if len_N == 0:
            return None
        elif len_N == 1:
            return TreeNode(nums[0])
        middle = len_N // 2
        node = TreeNode(nums[middle])
        left_node = self.sortedArrayToBST(nums[0:middle])
        right_node = self.sortedArrayToBST(nums[middle+1:])
        node.left = left_node
        node.right = right_node
        return node
