from typing import List

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        visited = set()
        q = []
        N = len(isWater)
        M = len(isWater[0])
        for i in range(N):
            for j in range(M):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    visited.add((i, j))

        level = -1
        while len(q) > 0:
            level += 1
            nq = []
            for i, j in q:
                isWater[i][j] = level
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
                        nq.append((nx, ny))
                        visited.add((nx, ny))
                q = nq
        return isWater


if __name__=="__main__":
    solution = Solution()
    print(solution.highestPeak([[1,0,0],[0,0,0]]))