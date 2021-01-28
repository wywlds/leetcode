from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counts = [0] * 101
        for num in nums:
            counts[num] += 1
        agg = 0
        for i in range(1, 101):
            cur = counts[i]
            counts[i] = agg
            agg += cur
        return [counts[num] for num in nums]