from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        start, end = points[0]
        n = 0
        for cur_s, cur_e in points[1:]:
            if cur_s > end:
                n += 1
                start, end = cur_s, cur_e
            else:
                start, end = max(start, cur_s), min(end, cur_e)

        n += 1
        return n