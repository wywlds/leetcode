from typing import List

import collections
UNKNOWN = 0
RED = 1
BLUE = 2
class Solution:

    def isBipartite(self, graph: List[List[int]]) -> bool:
        LEN = len(graph)
        colors = [UNKNOWN] * LEN
        for i, nodes in enumerate(graph):
            if colors[i] == UNKNOWN:
                queue = collections.deque([i])
                colors[i] = RED
                while queue:
                    cur = queue.popleft()
                    next_color = RED if colors[cur] == BLUE else BLUE
                    for node in graph[cur]:
                        if colors[node] == UNKNOWN:
                            colors[node] = next_color
                            queue.append(node)
                        elif colors[node] != next_color:
                            return False
        return True

if __name__=="__main__":
    solution = Solution()
    print(solution.isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))