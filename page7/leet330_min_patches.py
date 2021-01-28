from typing import List


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        x = 1
        ans = 0
        index = 0
        while x <= n:
            if nums[index] > x:
                ans += 1
                x = 2*x
            elif index < len(nums) and nums[index] <= x:
                x = x + nums[index]
                index += 1
        return ans

