from typing import List


class Solution:
    def orderOfLargestPlusSign(self, N: int, mines: List[List[int]]) -> int:
        banned = {tuple(mine) for mine in mines}
        dp = [[0] * N for _ in range(N)]
        ans = 0
        for j in range(0, N):
            count = 0
            for i in range(0, N):
                if (i, j) not in banned:
                    count += 1
                    dp[i][j] = count
                else:
                    count = 0
            count = 0
            for i in range(N-1, -1, -1):
                if (i, j) not in banned:
                    count += 1
                    dp[i][j] = min(dp[i][j], count)
                else:
                    count = 0
        for i in range(0, N):
            count = 0
            for j in range(0, N):
                if (i, j) not in banned:
                    count += 1
                    dp[i][j] = min(dp[i][j], count)
                else:
                    count = 0
            count = 0
            for j in range(N-1, -1, -1):
                if (i, j) not in banned:
                    count += 1
                    dp[i][j] = min(dp[i][j], count)
                    ans = max(ans, dp[i][j])
                else:
                    count = 0
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.orderOfLargestPlusSign(11, []))
