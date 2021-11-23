from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1, p2 = 0, 0
        last = None
        while p2 < len(nums):
            if nums[p2] != last:
                nums[p1] = nums[p2]
                last = nums[p2]
                p1 += 1
            p2 += 1
        return p1