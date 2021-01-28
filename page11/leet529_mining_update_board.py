from typing import List


import queue
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rounds = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (1,-1), (-1,-1), (-1,1)]
        pos_x, pos_y = click
        click_queue = queue.Queue()
        click_queue.put((pos_x, pos_y))

        X_SIZE = len(board)
        Y_SIZE = len(board[0])

        if board[pos_x][pos_y] == 'M':
            board[pos_x][pos_y] = 'X'
            return board
        else:
            board[pos_x][pos_y] = 'B'

        while not click_queue.empty():
            pos_x, pos_y = click_queue.get()

            count_star = 0
            for delta_x, delta_y in rounds:
                new_pos_x, new_pos_y = pos_x + delta_x, pos_y + delta_y
                if 0 <= new_pos_x < X_SIZE and 0 <= new_pos_y < Y_SIZE and board[new_pos_x][new_pos_y] == 'M':
                    count_star += 1

            if count_star > 0:
                board[pos_x][pos_y] = str(count_star)
                continue

            for delta_x, delta_y in rounds:
                new_pos_x, new_pos_y = pos_x + delta_x, pos_y + delta_y
                if 0 <= new_pos_x < X_SIZE and 0 <= new_pos_y < Y_SIZE and board[new_pos_x][new_pos_y] == 'E':
                    click_queue.put((new_pos_x, new_pos_y))
                    # 这里很重要，阻断多次进去队列计算
                    board[new_pos_x][new_pos_y] = 'B'
        return board

