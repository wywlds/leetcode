from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        N = len(matrix)
        if N == 0:
            return []
        M = len(matrix[0])
        ans = [[0] * N for _ in range(M)]
        for i in range(N):
            for j in range(M):
                ans[j][i] = matrix[i][j]
        return ans
