from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        if N == 0:
            return
        M = len(matrix[0])
        if M == 0:
            return
        i, j = -1, -1
        for ni in range(N):
            for nj in range(M):
                if matrix[ni][nj] == 0:
                    i, j = ni, nj
                    break
            if i != -1:
                break
        for ni in range(N):
            for nj in range(M):
                if matrix[ni][nj] == 0:
                    matrix[ni][j] = 0
                    matrix[i][nj] = 0
        for ni in range(N):
            if ni != i and matrix[ni][j] == 0:
                for nj in range(M):
                    matrix[ni][nj] = 0
        for nj in range(M):
            if nj != j and matrix[i][nj] == 0:
                for ni in range(N):
                    matrix[ni][nj] = 0
        for ni in range(N):
            matrix[ni][j] = 0

        for nj in range(M):
            matrix[i][nj] = 0

if __name__=="__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    solution = Solution()
    solution.setZeroes(matrix)
    print(matrix)