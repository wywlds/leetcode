from typing import List


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        N = len(nums)
        nums.append(1)
        nums.insert(0, 1)
        dp = [[0] * (N+2) for _ in range(N+2)]
        for i in range(N-1, -1, -1):
            for j in range(i+2, N+2):
                max_coin = 0
                for k in range(i+1, j):
                    sum = dp[i][k]
                    sum += dp[k][j]
                    sum += nums[i] * nums[k] * nums[j]
                    max_coin = max(max_coin, sum)
                dp[i][j] = max_coin
        return dp[0][N+1]

