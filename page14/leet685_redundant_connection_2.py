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
    def cycle(self, edges):
        disjoint = Disjoint(len(edges) + 1)
        for s, e in edges:
            p_s, p_e = disjoint.find(s), disjoint.find(e)
            # 如果在连接之前已经连接在一起了，即那么说明成环
            if p_s == p_e:
                return True
            else:
                disjoint.union(s, e)
        return False

    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        counter = {}
        d_end = -1
        for _, end in edges:
            if end in counter:
                d_end = end
            else:
                counter[end] = 1
        # 有一种可能性是指向了根节点
        if d_end == -1:
            disjoint = Disjoint(len(edges) + 1)
            for s, e in edges:
                p_s, p_e = disjoint.find(s), disjoint.find(e)
                if p_s == p_e:
                    return [s, e]
                else:
                    disjoint.union(s, e)
        # 另外一种可能性是指向了其他节点，因此必须有两个入度
        else:
            # 越后面优先级越高，因此从最后开始遍历起
            for i, [s, e] in enumerate(edges[::-1]):
                if e == d_end and not self.cycle(edges[::-1][0:i]+edges[::-1][i+1:]):
                    return [s, e]
        return None

