from typing import List


class Solution:
    def findLength(self, A: List[int], B: List[int]) -> int:
        len_A = len(A)
        len_B = len(B)
        dp = [[0] * (len_B + 1) for _ in range(len_A + 1)]
        max_len = 0
        for i in range(len_A-1, -1, -1):
            for j in range(len_B-1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
                    max_len = max(max_len, dp[i][j])

        return max_len