from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        count_inverse = 0
        for i in range(-1, len(nums)):
            if nums[i + 1] < nums[i]:
                count_inverse += 1
        return count_inverse <= 1