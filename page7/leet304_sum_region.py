from typing import List


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        M = len(matrix)
        N = len(matrix[0])
        self.aggs = [[0] * (N + 1) for _ in range(M + 1)]
        for i in range(1, M+1):
            for j in range(1, N + 1):
                self.aggs[i][j] = self.aggs[i - 1][j] + self.aggs[i][j - 1] - self.aggs[i - 1][j - 1] + matrix[i - 1][j
                                                                                                                   - 1]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.aggs[row2 + 1][col2 + 1] - self.aggs[row1][col2 + 1] - self.aggs[row2 + 1][col1] + self.aggs[
            row1][col1]

if __name__=="__main__":
    matrix = [
        [3, 0, 1, 4, 2],
        [5, 6, 3, 2, 1],
        [1, 2, 0, 1, 5],
        [4, 1, 0, 1, 7],
        [1, 0, 3, 0, 5]
    ]
    solution = NumMatrix(matrix)
    print(solution.sumRegion(2, 1, 4, 3))