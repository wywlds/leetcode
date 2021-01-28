from typing import List


class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        start = 0
        end = 0
        last = float("-inf")
        max_len = 1
        for i, num in enumerate(nums):
            if num > last:
                end = i
            else:
                max_len = max(end - start + 1, max_len)
                start, end = i, i
            last = num
        max_len = max(max_len, end-start+1)
        return max_len
