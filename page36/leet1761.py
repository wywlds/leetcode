from typing import List
from collections import defaultdict


class Solution:
    def minTrioDegree(self, n: int, edges: List[List[int]]) -> int:
        edge_cnt_dict = defaultdict(lambda: 0)
        next_nodes_dict = defaultdict(lambda : set())
        for s, t in edges:
            edge_cnt_dict[s] += 1
            edge_cnt_dict[t] += 1
            next_nodes_dict[s].add(t)
            next_nodes_dict[t].add(s)
        ans = -1
        for s, t in edges:
            for d in next_nodes_dict[s].intersection(next_nodes_dict[t]):
                deg = edge_cnt_dict[d] + edge_cnt_dict[s] + edge_cnt_dict[t] - 6
                if ans == -1:
                    ans = deg
                else:
                    ans = min(ans, deg)
        return ans


if __name__=="__main__":
    n = 6
    edges = [[1,2],[1,3],[3,2],[4,1],[5,2],[3,6]]
    solution = Solution()
    print(solution.minTrioDegree(6, edges))

