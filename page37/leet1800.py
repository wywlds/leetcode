from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        agg = 0
        ans = 0
        for i, num in enumerate(nums):
            if i > 0 and nums[i] <= nums[i - 1]:
                agg = 0
            agg += num
            ans = max(ans, agg)
        return ans