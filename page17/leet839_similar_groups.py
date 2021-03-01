from typing import List

class UnionFind():
    def __init__(self, n):
        self.cnt_group = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        self.parents[x] = self.find(self.parents[x])
        return self.parents[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px != py:
            self.parents[py] = px
            self.cnt_group -= 1

class Solution:

    def isSimilar(self, sa, sb):
        cnt = 0
        for cha, chb in zip(sa, sb):
            if cha != chb:
                cnt += 1
                if cnt > 2:
                    return False
        return True

    def numSimilarGroups(self, strs: List[str]) -> int:
        uf = UnionFind(len(strs))
        for i, sa in enumerate(strs):
            for j, sb in enumerate(strs):
                if i != j:
                    if self.isSimilar(sa, sb):
                        uf.union(i, j)
        return uf.cnt_group

if __name__=="__main__":
    strs = ["tars","rats","arts","star"]
    solution = Solution()
    print(solution.numSimilarGroups(strs))