from typing import List


class Disjoint:
    def __init__(self, N):
        self.p = [-1] * N

    def find(self,i):
        while self.p[i] != -1:
            i = self.p[i]
        return i

    def union(self, i, j):
        parent_i, parent_j = self.find(i), self.find(j)
        if parent_i != parent_j:
            self.p[parent_j] = parent_i

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        disjoint = Disjoint(len(edges) + 1)
        for i, j in edges:
            parent_i, parent_j = disjoint.find(i), disjoint.find(j)
            if parent_i == parent_j:
                return [i, j]
            else:
                disjoint.union(i, j)
        return None