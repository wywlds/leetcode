from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        empty_list = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_list.append((i, j))

        def possible(i, j, num):
            for t_j in range(9):
                if board[i][t_j] == num:
                    return False
            for t_i in range(9):
                if board[t_i][j] == num:
                    return False
            base_i, base_j = i//3, j//3
            for d_i in range(3):
                for d_j in range(3):
                    n_i, n_j = base_i * 3 + d_i, base_j * 3 + d_j
                    if board[n_i][n_j] == num:
                        return False
            return True

        def dfs(li):
            if li == len(empty_list):
                return True
            i, j = empty_list[li]
            for num in range(1, 10):
                if possible(i, j, str(num)):
                    board[i][j] = str(num)
                    if dfs(li + 1):
                        return True
                    board[i][j] = '.'
            return False
        print(dfs(0))


if __name__=="__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
     [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
     ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
     [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
     [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    solution = Solution()
    solution.solveSudoku(board)
    pass