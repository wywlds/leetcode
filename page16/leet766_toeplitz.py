from typing import List


class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        N, M = len(matrix), len(matrix[0])
        if N == 0:
            return True
        M = len(matrix[0])
        value_dic = {}
        for i in range(N):
            for j in range(M):
                if i - j not in value_dic:
                    value_dic[i - j] = matrix[i][j]
                elif matrix[i][j] != value_dic:
                    return False
        return True