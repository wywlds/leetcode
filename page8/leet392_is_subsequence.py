class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        if m == 0 and n == 0:
            return True
        if m == 0:
            return False
        memo = [[m] * 26 for _ in range(m)]
        for i in range(m-1, -1, -1):
            for j in range(26):
                if t[i] == chr(ord('a') + j):
                    memo[i][j] = i
                else:
                    memo[i][j] = memo[i+1][j] if i < m - 1 else m
        j = 0
        for i, ch in enumerate(s):
            if j >= m:
                return False
            if memo[j][ord(ch) - ord('a')] == m:
                return False
            else:
                j = memo[j][ord(ch) - ord('a')]+1
        return True


if __name__=="__main__":
    solution = Solution()
    solution.isSubsequence("abc", "ahbgdc")