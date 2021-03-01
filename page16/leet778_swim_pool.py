from typing import List

class UnionFind():
    def __init__(self, N, M):
        self.parents = [-1] * (N * M)
        self.M = M
        self.N = N

    def find(self, x, y):
        i = x * self.M + y
        if self.parents[i] < 0:
            return i
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, x1, y1, x2, y2):
        p1 = self.find(x1, y1)
        p2 = self.find(x2, y2)
        if p1 < p2:
            self.parents[p2] = p1
        elif p2 < p1:
            self.parents[p1] = p2
        return self.find(self.N - 1, self.M - 1) == 0

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        links = []
        for x in range(N):
            for y in range(M):
                if x != N - 1:
                    links.append((max(grid[x+1][y], grid[x][y]), x, y, x+1, y))
                if y != M - 1:
                    links.append((max(grid[x][y+1], grid[x][y]), x, y, x, y + 1))
        links.sort()
        union_f = UnionFind(N, M)
        for ans, x1, y1, x2, y2 in links:
            if union_f.union(x1, y1, x2, y2):
                return ans
        return -1