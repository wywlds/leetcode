from typing import List

import heapq
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M = len(matrix)
        N = len(matrix[0])
        if M == 0 or N == 0:
            return 0
        memo = [[1] * N for _ in range(M)]
        q = []
        for i in range(M):
            for j in range(N):
                q.append((matrix[i][j], i, j))
        heapq.heapify(q)
        max_step = 1
        while q:
            (num, i, j) = heapq.heappop(q)
            step = memo[i][j]
            for d_i, d_j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                n_i, n_j = i + d_i, j + d_j
                if 0 <= n_i < M and 0 <= n_j < N and matrix[n_i][n_j] > num:
                    memo[n_i][n_j] = max(memo[n_i][n_j], step + 1)
                    max_step = max(max_step, step + 1)

        return max_step