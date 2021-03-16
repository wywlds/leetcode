from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        M = [[0] * n for _ in range(n)]
        def get_dir(step):
            if step == 0:
                return 0, 1
            elif step == 1:
                return 1, 0
            elif step == 2:
                return 0, -1
            else:
                return -1, 0
        blocking_x = [-1, n]
        blocking_y = [-1, n]

        x, y = 0, 0
        ans = 1
        while True:
            M[x][y] = ans
            ans += 1
            dx, dy = get_dir(step)
            if (x + dx) in blocking_x or (y + dy) in blocking_y:
                if step in [0, 2]:
                    blocking_x.append(x)
                else:
                    blocking_y.append(y)
                step = (step + 1) % 4
                dx, dy = get_dir(step)
                if (x + dx) in blocking_x or (y + dy) in blocking_y:
                    break
            x, y = x + dx, y + dy
        return M