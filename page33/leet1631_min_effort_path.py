from typing import List

import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        h = [(0, 0, 0)]
        visited = set()
        N, M = len(heights), len(heights[0])
        while len(h) > 0:
            cur_effort, x, y = heapq.heappop(h)
            if (x, y) == (N - 1, M - 1):
                return cur_effort
            if (x, y) not in visited:
                visited.add((x, y))
                if (x + 1, y) not in visited and x + 1 < N:
                    heapq.heappush(h, (max(cur_effort, abs(heights[x+1][y] - heights[x][y])), x + 1, y))
                if (x - 1, y) not in visited and x - 1 >= 0:
                    heapq.heappush(h, (max(cur_effort, abs(heights[x-1][y] - heights[x][y])), x - 1, y))
                if (x, y + 1) not in visited and y + 1 < M:
                    heapq.heappush(h, (max(cur_effort, abs(heights[x][y + 1] - heights[x][y])), x, y + 1))
                if (x, y - 1) not in visited and y - 1 >= 0:
                    heapq.heappush(h, (max(cur_effort, abs(heights[x][y - 1] - heights[x][y])), x, y - 1))
        return 0


if __name__=="__main__":
    heights =[[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]
    solution = Solution()
    print(solution.minimumEffortPath(heights))