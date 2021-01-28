from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        min1, min2 = cost[0], cost[1]
        for x in cost[2:]:
            cur_cost = min(min1, min2) + x
            min1 = min2
            min2 = cur_cost
        return min(min1, min2)