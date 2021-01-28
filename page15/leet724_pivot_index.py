from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        agg_l = [0] * (len(nums) + 1)
        tmp = 0
        n = len(nums)
        for i, num in enumerate(nums):
            tmp += num
            agg_l[i + 1] = tmp
        for i in range(1, len(nums) + 1):
            if agg_l[i - 1] * 2 == agg_l[n] - nums[i]:
                return i - 1
        return -1
