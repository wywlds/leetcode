class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        d = [[1] * (k + 1) for _ in range(n + 1)]
        for j in range(1, k + 1):
            d[0][j] = 0
        for i in range(1, n + 1):
            for j in range(1, k + 1):
                part1 = d[i-1][j] + d[j-1][i]
                part2 = d[i-1][j-i] if j-i>=0 else 0
                d[i][j] = part1 - part2
        return d[n][k]