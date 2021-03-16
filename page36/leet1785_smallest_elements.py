from typing import List

import math
class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        sum_cur = sum(nums)
        delta = goal - sum_cur
        return math.ceil(abs(delta) / limit)