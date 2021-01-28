class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        root = 10**9 + 7

        cur_layer = [(i,j,0,1)]
        counter_map = [[None] * n for _ in range(m)]

        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        count = 0
        for i in range(N):
            new_i = i + 1
            new_layer = []
            for i, j, _, c in cur_layer:
                c = c % root
                for d_i, d_j in dirs:
                    n_i, n_j = i + d_i, j + d_j
                    if 0 <= n_i < n and 0 <= n_j < m:
                        if counter_map[n_i][n_j] is None or counter_map[n_i][n_j][3] != new_i:
                            counter_map[n_i][n_j] = [n_i, n_j, new_i, c]
                            new_layer.append(counter_map[n_i][n_j])
                        else:
                            counter_map[n_i][n_j][3] += c
                    else:
                        count = (count + c) % root
            cur_layer = new_layer
        return count

