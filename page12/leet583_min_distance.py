class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1) + 1
        M = len(word2) + 1
        dp = [[0] * M for _ in range(N)]
        for i in range(1,N):
            for j in range(1,M):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return M + N - 2 - 2*dp[N-1][M-1]