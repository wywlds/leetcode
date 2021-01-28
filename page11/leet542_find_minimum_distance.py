from typing import List

import queue
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        updated = set()
        waiting_q = queue.Queue()

        N = len(matrix)
        M = len(matrix[0])

        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        for x in range(N):
            for y in range(M):
                if matrix[x][y] == 0:
                    updated.add((x,y))
                    waiting_q.put((x,y))
        while not waiting_q.empty():
            x, y = waiting_q.get()
            for dx, dy in directions:
                nx = x + dx
                ny = y + dy
                if 0<=nx<N and 0<=ny<M and (nx, ny) not in updated:
                    matrix[nx][ny] = matrix[x][y] + 1
                    updated.add((nx, ny))
                    waiting_q.put((nx, ny))
        return matrix