from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for i in range(0, (N + 1) // 2):
            for j in range(0, N // 2):
                index_seq = [(i, j), (j, N-1-i), (N-1-i, N-1-j), (N-1-j, i)]
                last_value = matrix[index_seq[-1][0]][index_seq[-1][1]]
                for k in range(4):
                    cur_value = matrix[index_seq[k][0]][index_seq[k][1]]
                    matrix[index_seq[k][0]][index_seq[k][1]] = last_value
                    last_value = cur_value

if __name__=="__main__":
    solution = Solution()
    matrix = [[ 5, 1, 9,11],[ 2, 4, 8,10],[13, 3, 6, 7],[15,14,12,16]]
    solution.rotate(matrix)
    print(matrix)

