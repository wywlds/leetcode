from typing import List

import heapq
import collections
class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        q = []
        self.M = len(forest)
        self.N = len(forest[0])
        for i in range(self.M):
            for j in range(self.N):
                item = forest[i][j]
                if item != 0:
                    heapq.heappush(q, (item, i, j))
        start_i, start_j = 0, 0
        t_dist = 0
        while q:
            _, next_i, next_j = heapq.heappop(q)
            dist = self.dist(forest, start_i, start_j, next_i, next_j)
            if dist != -1:
                t_dist += dist
                start_i, start_j = next_i, next_j
            else:
                return -1
        return t_dist

    def dist(self, forest, start_i, start_j, tar_i, tar_j):
        visited = set()
        q = collections.deque()
        q.append((start_i, start_j, 0))
        visited.add((start_i, start_j))
        while q:
            cur_i, cur_j, dist = q.popleft()
            if cur_i == tar_i and cur_j == tar_j:
                return dist
            for delta_i, delta_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_i, new_j = cur_i + delta_i, cur_j + delta_j
                if 0 <= new_i < self.M and 0 <= new_j < self.N and (new_i, new_j) not in visited and forest[new_i][
                    new_j] > 0:
                    visited.add((new_i, new_j))
                    q.append((new_i, new_j, dist + 1))
        return -1


if __name__=="__main__":
    solution = Solution()
    print(solution.cutOffTree([[1,2,3],[0,0,4],[7,6,5]]))

