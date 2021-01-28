from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == 0 or len(nums) < k:
            return 0
        sum_v = sum(nums[0:k])
        max_sum = sum_v
        for i in range(0, len(nums) - k):
            sum_v = sum_v - nums[i] + nums[i + k]
            max_sum = max(sum_v, max_sum)
        return max_sum /k