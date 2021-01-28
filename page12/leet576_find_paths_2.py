class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        root = 10**9 + 7

        cur_layer = [[0] * n for _ in range(m)]
        cur_layer[i][j] = 1

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        for i in range(N):
            new_layer = [[0] * n for _ in range(m)]
            for i in range(m):
                for j in range(m):
                    c = cur_layer[i][j]
                    for d_i, d_j in dirs:
                        n_i, n_j = i + d_i, j+d_j
                        if n_i == -1 or n_j == -1 or n_i == m or n_j == n:
                            count += c
                        else:
                            new_layer[n_i][n_j] += c
        return count % root