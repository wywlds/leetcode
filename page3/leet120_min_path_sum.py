from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        last = [0]
        layer_cnt = len(triangle)
        for i in range(layer_cnt):
            column_cnt = i + 1
            cur = []
            for j in range(column_cnt):
                if j == 0:
                    cur.append(last[0] + triangle[i][j])
                elif j == column_cnt - 1:
                    cur.append(last[j-1] + triangle[i][j])
                else:
                    cur.append(min(last[j], last[j - 1]) + triangle[i][j])
            last = cur
        return min(last)
