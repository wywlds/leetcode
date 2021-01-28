from typing import List

class UnionFind():
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        p_x = self.find(x)
        p_y = self.find(y)
        if p_x != p_y:
            self.parents[p_y] = p_x

    def set_count(self):
        c = 0
        for p in self.parents:
            if p == -1:
                c += 1
        return c

class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1
        union_f = UnionFind(n)
        for x, y in connections:
            union_f.union(x, y)
        return union_f.set_count() - 1