from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        M = len(dungeon)
        N = len(dungeon[0])
        dp = [1] * N

        dp[N-1] = max(1 - dungeon[M - 1][N - 1], 1)
        for j in range(N-2, -1, -1):
            dp[j] = max(dp[j + 1] - dungeon[M-1][j], 1)
        for i in range(M - 2, -1, -1):
            dp[N-1] = max(dp[N-1] - dungeon[i][N-1], 1)
            for j in range(N - 2, -1, -1):
                dp[j] = max(min(dp[j+1], dp[j]) - dungeon[i][j], 1)
        return dp[0]

if __name__=="__main__":
    solution = Solution()
    solution.calculateMinimumHP([[0, -3]])