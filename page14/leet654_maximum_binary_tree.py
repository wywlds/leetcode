from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        max_num = max(nums)
        max_index = nums.index(max_num)
        left_list = nums[:max_index]
        right_list = nums[max_index+1:]
        root = TreeNode(max_num)
        root.left = self.constructMaximumBinaryTree(left_list)
        root.right = self.constructMaximumBinaryTree(right_list)
        return root