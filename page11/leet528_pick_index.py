from typing import List

import random
import bisect
class Solution:

    def __init__(self, w: List[int]):
        self.agg_w = 0
        self.agg_ws = []
        for i_w in w:
            self.agg_w += i_w
            self.agg_ws.append(self.agg_w)

    def pickIndex(self) -> int:
        w = random.randint(0, self.agg_w - 1)
        i = bisect.bisect_right(self.agg_ws, w)
        return i


if __name__=="__main__":
    solution = Solution([1, 9])
    for i in range(20):
        print(solution.pickIndex())