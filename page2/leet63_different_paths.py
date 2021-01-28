from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        memory = [[0] * N for _ in range(M)]
        memory[0][0] = 1
        for i in range(M):
            if obstacleGrid[i][0] != 1:
                memory[i][0] = 1
            else:
                break
        for j in range(N):
            if obstacleGrid[0][j] != 1:
                memory[0][j] = 1
            else:
                break
        for i in range(1, M):
            for j in range(1, N):
                if obstacleGrid[i][j] == 1:
                    continue
                else:
                    memory[i][j] = memory[i-1][j] + memory[i][j-1]
        return memory[M-1][N-1]