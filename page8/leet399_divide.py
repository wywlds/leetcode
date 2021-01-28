from typing import List
from collections import defaultdict


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edge_map = defaultdict(list)
        for (start, end), value in zip(equations, values):
            edge_map[start].append((end, value))
            edge_map[end].append((start, 1.0/value))
        ans = []
        for start, end in queries:
            ans.append(self.calcDivide(start, end, edge_map))
        return ans

    def calcDivide(self, start, end, edge_map):
        if start not in edge_map or end not in edge_map:
            return -1.0
        q = [(start, 1.0)]
        visited = set([start])
        while len(q) > 0:
            cur_node, value = q.pop(0)
            if cur_node == end:
                return value
            for next_node, next_value in edge_map[cur_node]:
                if next_node not in visited:
                    q.append((next_node, next_value * value))
                    visited.add(next_node)
        return -1.0


if __name__=="__main__":
    equations = [["a","aa"]]
    values = [9.0]
    queries = [["aa","a"],["aa","aa"]]
    solution = Solution()
    print(solution.calcEquation(equations, values, queries))