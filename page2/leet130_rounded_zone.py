from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        M = len(board)
        N = len(board[0])
        o_set = set()
        bound_set = set()
        for i in range(M):
            for j in range(N):
                if board[i][j] == 'O':
                    o_set.add((i, j))
                    if i in [0, M-1] or j in [0, N-1]:
                        bound_set.add((i, j))
        def dfs(i, j):
            if (i, j) in o_set:
                o_set.remove((i, j))
                for d_i, d_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    n_i, n_j = i + d_i, j + d_j
                    if (n_i, n_j) in o_set:
                        dfs(n_i, n_j)
        for i, j in bound_set:
            dfs(i, j)
        for i, j in o_set:
            board[i][j] = 'M'