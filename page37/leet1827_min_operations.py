from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        last = nums[0]
        ans = 0
        for i, num in enumerate(nums):
            if num < last:
                nums[i] = last
                ans += (last - num)
            last = nums[i] + 1
        return ans