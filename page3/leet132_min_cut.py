class Solution:
    def minCut(self, s: str) -> int:
        N = len(s)
        g = [[True] * N for _ in range(N)]
        for i in range(N, -1, -1):
            for j in range(i + 1, N):
                g[i][j] = g[i+1][j-1] and s[i] == s[j]

        INF = 0x3f3f3f3f
        dp = [INF] * N
        for i in range(N):
            if g[0][i]:
                dp[i] = 1
            else:
                for j in range(0, N - 1):
                    if g[j + 1][i]:
                        dp[i] = min(dp[j] + 1, dp[i])
        return dp[N - 1] - 1


if __name__=="__main__":
    solution = Solution()
    print(solution.minCut("abacbca"))