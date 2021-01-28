from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        spare = 0
        min_spare = float('inf')
        min_index = 0
        for i, (g, c) in enumerate(zip(gas, cost)):
            spare += (g - c)
            if spare < min_spare:
                min_index = i
                min_spare = spare
        return min_index + 1 if spare >= 0 else -1