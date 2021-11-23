from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p1, p2 = 0, 0
        while p2 < len(nums):
            if p1 < 2 or nums[p1 - 2] != nums[p2]:
                nums[p1] = nums[p2]
                p1 += 1
            p2 += 1
        return p1