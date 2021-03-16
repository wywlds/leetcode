from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        step = 0
        def get_dir(step):
            if step == 0:
                return 0, 1
            elif step == 1:
                return 1, 0
            elif step == 2:
                return 0, -1
            else:
                return -1, 0
        blocking_x = [-1, len(matrix)]
        blocking_y = [-1, len(matrix[0])]

        x, y = 0, 0
        ans = []
        while True:
            ans.append(matrix[x][y])
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
        return ans


if __name__=="__main__":
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    solution = Solution()
    print(solution.spiralOrder(matrix))