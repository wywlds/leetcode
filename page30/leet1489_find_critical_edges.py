from typing import List


class Tarjan:
    def __init__(self, gn, next_nodes, edge_ids):
        self.gn = gn
        self.next_nodes = next_nodes
        self.edge_ids = edge_ids
        self.ts = 0
        self.dfn = [-1] * gn
        self.low = [-1] * gn
        self.ans = []

    def critical_edges(self):
        for g in range(self.gn):
            if self.dfn[g] == -1:
                self.dfs(g, -1)
        return self.ans

    def dfs(self, g, parent_edge_id):
        self.ts += 1
        self.dfn[g] = self.low[g] = self.ts
        for next_g, edge_id in zip(self.next_nodes[g], self.edge_ids[g]):
            if self.dfn[next_g] == -1:
                self.dfs(next_g, edge_id)
                self.low[g] = min(self.low[g], self.low[next_g])
                if self.low[next_g] > self.dfn[g]:
                    self.ans.append(edge_id)
            elif edge_id != parent_edge_id:
                self.low[g] = min(self.low[g], self.dfn[next_g])


class UnionFind:
    def __init__(self, n):
        self.parents = [-1] * n

    def find(self, i):
        if self.parents[i] == -1:
            return i
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i ,j):
        parent_i = self.find(i)
        parent_j = self.find(j)
        if parent_i == parent_j:
            return False
        self.parents[parent_j] = parent_i
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i, edge in enumerate(edges):
            edge.append(i)
        edges.sort(key=lambda l:l[2])

        LEN = len(edges)
        i = 0
        labels = [0] * LEN
        union_set = UnionFind(n)

        cs = []
        while i < LEN:
            j = i
            while j < LEN and edges[j][2] == edges[i][2]:
                j += 1
            gn = 0
            g_dic = {}
            for k in range(i, j):
                x, y = union_set.find(edges[k][0]), union_set.find(edges[k][1])
                if x != y:
                    if x not in g_dic:
                        g_dic[x] = gn
                        gn += 1
                    if y not in g_dic:
                        g_dic[y] = gn
                        gn += 1
                else:
                    labels[edges[k][3]] = -1

            next_nodes = [[] for _ in range(gn)]
            edge_index = [[] for _ in range(gn)]
            for k in range(i, j):
                x, y = union_set.find(edges[k][0]), union_set.find(edges[k][1])
                if x != y:
                    next_nodes[g_dic[x]].append(g_dic[y])
                    edge_index[g_dic[x]].append(edges[k][3])
                    next_nodes[g_dic[y]].append(g_dic[x])
                    edge_index[g_dic[y]].append(edges[k][3])

            targan = Tarjan(gn, next_nodes, edge_index)
            critial_edges = targan.critical_edges()
            cs.extend(critial_edges)
            for critial_edge in critial_edges:
                labels[critial_edge] = 1
            for k in range(i, j):
                union_set.union(edges[k][0], edges[k][1])
            i = j
        pcs = [i for i in range(LEN) if labels[i] == 0]
        return [cs, pcs]