from typing import List

class UnionFind(object):

    def __init__(self, N):
        self.N = 0
        self.parents = [-1] * N

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        parent_x = self.find(x)
        parent_y = self.find(y)
        if parent_x != parent_y:
            self.parents[parent_y] += self.parents[parent_x]
            self.parents[parent_x] = parent_y

    def count(self):
        ans = 0
        for p in self.parents:
            if p < 0:
                ans += ((-p) // 2 - 1)
        return ans


class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        LEN = len(row)
        uf = UnionFind(LEN)
        for i in range(0, LEN, 2):
            uf.union(i, i + 1)

        for i in range(0, LEN, 2):
            uf.union(row[i], row[i + 1])
        return uf.count()

if __name__=="__main__":
    row = [0, 2, 1, 3]
    solution = Solution()
    print(solution.minSwapsCouples(row))