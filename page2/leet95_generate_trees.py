from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        nums = list(range(1, n+1, 1))
        return self.generateTreesInternal(nums)

    def generateTreesInternal(self, nums):
        if len(nums) == 0:
            return [None]
        nodes = []
        for i, num in enumerate(nums):
            for node_l in self.generateTreesInternal(nums[0:i]):
                for node_r in self.generateTreesInternal(nums[i+1:]):
                    node = TreeNode(num)
                    node.left = node_l
                    node.right = node_r
                    nodes.append(node)
        return nodes


if __name__=="__main__":
    solution = Solution()
    solution.generateTrees(10)