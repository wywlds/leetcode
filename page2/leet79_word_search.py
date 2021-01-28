from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        M = len(board)
        N = len(board[0])
        visited = set()
        def dfs(x, y, word):
            if len(word) == 0:
                return True
            char0 = word[0]
            if char0 == board[x][y]:
                word = word[1:]
                visited.add((x, y))
                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy
                    if not (nx, ny) in visited and 0 <= nx < M and 0 <= ny < N:
                        if dfs(nx, ny, word):
                            return True
                visited.remove((x, y))
                return False
            else:
                return False

        for i in range(M):
            for j in range(N):
                if dfs(i, j, word):
                    return True