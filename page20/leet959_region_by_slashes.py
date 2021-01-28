from typing import List


class UnionFind(object):
    def __init__(self, N):
        self.parents = [[[None] * 4 for _ in range(N)] for _ in range(N)]
        self.N = N

    def find(self, i ,j, k):
        if self.parents[i][j][k] is None:
            return (i, j, k)
        self.parents[i][j][k] = self.find(*self.parents[i][j][k])
        return self.parents[i][j][k]

    def union(self, i1, j1, k1, i2, j2, k2):
        p1 = self.find(i1, j1, k1)
        p2 = self.find(i2, j2, k2)
        if p1 != p2:
            self.parents[p2[0]][p2[1]][p2[2]] = p1

    def set_count(self):
        ans = 0
        for i in range(self.N):
            for j in range(self.N):
                for k in range(4):
                    if self.parents[i][j][k] is None:
                        ans += 1
        return ans

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        uf = UnionFind(N)
        for i, g in enumerate(grid):
            cur = 0
            for j in range(N):
                if g[cur] == '/':
                    cur += 1
                    uf.union(i, j, 0, i, j, 1)
                    uf.union(i, j, 2, i, j, 3)
                elif g[cur] == ' ':
                    cur += 1
                    uf.union(i, j, 0, i, j, 1)
                    uf.union(i, j, 0, i, j, 2)
                    uf.union(i, j, 0, i, j, 3)
                elif g[cur] == '\\':
                    cur += 1
                    uf.union(i, j, 1, i, j, 2)
                    uf.union(i, j, 0, i, j, 3)
                if j != N - 1:
                    uf.union(i, j, 2, i, j + 1, 0)
                if i != N - 1:
                    uf.union(i, j, 3, i + 1, j, 1)
        return uf.set_count()

if __name__=="__main__":
    grid = ["\\/","/\\"]
    solution = Solution()
    print(solution.regionsBySlashes(grid))