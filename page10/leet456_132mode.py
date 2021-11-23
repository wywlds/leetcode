from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        mem = [0] * len(nums)
        minv = nums[0]
        for i, num in enumerate(nums):
            mem[i] = minv
            minv = min(minv, num)

        s = [nums[-1]]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > minv[i]:
                while s and s[-1] <= minv[1]:
                    s.pop()
                if s and s[-1] < nums[i]:
                    return True
                s.append(nums[i])
        return False
