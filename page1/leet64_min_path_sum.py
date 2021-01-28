from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        M = len(grid)
        if M == 0:
            return 0
        N = len(grid[0])
        memo = [0] * N
        for i, num in enumerate(grid[0]):
            memo[i] = memo[i-1] + num
        for i, nums in enumerate(grid):
            if i == 0:
                continue
            for j, num in enumerate(nums):
                if j == 0:
                    memo[0] = memo[0] + num
                else:
                    memo[j] = min(memo[j], memo[j-1]) + num
        return memo[-1]