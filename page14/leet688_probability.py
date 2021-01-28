class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp_pre = [[1] * N for _ in range(N)]
        dp_next = [[0] * N for _ in range(N)]
        for t in range(K):
            for i in range(N):
                for j in range(N):
                    for delta_x, delta_y in [(1, 2), (2, 1), (-1, 2), (2, -1), (1, -2), (-2, 1), (-1, -2), (-2, -1)]:
                        n_x, n_y = i + delta_x, i + delta_y
                        if 0<=n_x<N and 0<=n_y<N:
                            dp_next[i][j] += dp_pre[n_x][n_y] / 8.0
            tmp = dp_pre
            dp_pre = dp_next
            dp_next = tmp

        return dp_pre[r][c]