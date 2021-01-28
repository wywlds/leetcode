from typing import List

class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        self.parents[py] = px
        return True

    def connected(self):
        ans = 0
        for p in self.parents[1:]:
            if p < 0:
                ans += 1
        return ans == 1

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(reverse=True)
        labels = [0] * len(edges)
        union_find = UnionFind(n + 1)
        for i, (type, s, e) in enumerate(edges):
            if type != 2 and union_find.union(s, e):
                labels[i] = 1
        if not union_find.connected():
            return -1
        union_find_2 = UnionFind(n + 1)
        for i, (type, s, e) in enumerate(edges):
            if type != 1 and union_find_2.union(s, e):
                labels[i] = 1
        if not union_find_2.connected():
            return -1

        ans = len(edges) - sum(labels)
        return ans

if __name__=="__main__":
    n = 4
    edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
    solution = Solution()
    print(solution.maxNumEdgesToRemove(n, edges))
