from typing import List

from collections import defaultdict
class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        edge_cnt = defaultdict(lambda: 0)
        n_count = [0] * n
        for edge in edges:
            edge.sort()
            edge = (edge[0], edge[1])
            edge_cnt[edge] += 1
            n_count[edge[0] - 1] += 1
            n_count[edge[1] - 1] += 1
        c_l = sorted(n_count)

        anss = []
        for query in queries:
            ans = 0
            l, r = 0, n - 1
            while l < n - 1:
                r = max(l+1, r)
                while r > l and c_l[l] + c_l[r] > query:
                    r -= 1
                ans += (n - r - 1)
                l += 1
            for (s, e), c in edge_cnt.items():
                if (n_count[s - 1] + n_count[e - 1]) > query and (n_count[s - 1] + n_count[e - 1] - c) <= query:
                    ans -= 1
            anss.append(ans)
        return anss

if __name__=="__main__":
    # n = 4
    # edges = [[1,2],[2,4],[1,3],[2,3],[2,1]]
    # queries = [2,3]
    # n = 5
    # edges = [[1,5],[1,5],[3,4],[2,5],[1,3],[5,1],[2,3],[2,5]]
    # queries = [1,2,3,4,5]

    n = 5
    edges = [[4,5],[1,3],[1,4]]
    queries = [0,1,0,0,1,1,0,0,0,0,1,0,0,1,0,1,1,2]
    solution = Solution()
    print(solution.countPairs(n, edges, queries))