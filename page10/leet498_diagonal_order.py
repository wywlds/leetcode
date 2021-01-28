from typing import List

# 值得纪念，先想清楚，不要随意地调入if-else中去
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix)
        if M == 0:
            return []

        N = len(matrix[0])
        result = []
        for i in range(M + N - 1):
            if i % 2 == 0:
                x_sign, y_sign = -1, 1
                start_x, start_y = (i, 0) if i < M else (M - 1, i - M + 1)
                end_x, end_y = (0, i) if i < N else (i - N + 1, N - 1)
            else:
                x_sign, y_sign = 1, -1
                start_x, start_y = (0, i) if i < N else (i - N + 1, N - 1)
                end_x, end_y = (i, 0) if i < M else (M - 1, i - M + 1)
            while True:
                result.append(matrix[start_x][start_y])
                if start_x == end_x and start_y == end_y:
                    break
                start_x += x_sign
                start_y += y_sign
        return result



if __name__=="__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    solution = Solution()
    result = solution.findDiagonalOrder(matrix)
    print(result)