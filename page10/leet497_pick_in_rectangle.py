from typing import List
import random
import bisect

class Solution:
    def __init__(self, rects: List[List[int]]):
        self.rects = rects

        agg_p_count = 0
        counts = []
        for x1, y1, x2, y2 in rects:
            p_count = (y2-y1+1) * (x2-x1+1)
            agg_p_count += p_count
            counts.append(agg_p_count)
        self.counts = counts
        self.p_count = agg_p_count

    def pick(self) -> List[int]:
        random_num = random.randint(0, self.p_count - 1)
        rect_index = bisect.bisect_right(self.counts, random_num)
        x1, y1, x2, y2 = self.rects[rect_index]
        if rect_index != 0:
            residu = random_num - self.counts[rect_index - 1]
        else:
            residu = random_num

        delta_y = int(residu / (x2 - x1 + 1))
        delta_x = residu % (x2 - x1 + 1)
        x = x1 + delta_x
        y = y1 + delta_y
        return [x, y]