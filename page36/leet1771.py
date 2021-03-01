class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        s = word1 + word2
        return self.longestPalindromeSubseq(s, n)

    def longestPalindromeSubseq(self, s: str, m) -> int:
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = 1
            for j in range(i - 1, -1, -1):
                if s[j] == s[i]:
                    dp[j][i] = 2 + dp[j + 1][i - 1]
                else:
                    dp[j][i] = max(dp[j + 1][i], dp[j][i - 1])
        ans = 0
        for i in range(n):
            for j in range(i + 1, n):
                if i < m <= j and s[i] == s[j]:
                    ans = max(dp[i][j], ans)
        return ans

if __name__=="__main__":
    word1 = "aa"
    word2 = "bb"
    solution = Solution()
    print(solution.longestPalindrome(word1, word2))