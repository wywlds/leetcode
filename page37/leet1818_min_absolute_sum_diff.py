from typing import List

import bisect
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        slist = list(set(nums1))
        slist.sort()

        sum_delta = 0
        for num1, num2 in zip(nums1, nums2):
            sum_delta += abs(num1 - num2)

        max_delta = 0
        for num1, num2 in zip(nums1, nums2):
            ind = bisect.bisect_left(slist, num2)
            if ind < len(slist):
                max_delta = max(max_delta, abs(num1 - num2) - abs(slist[ind] - num2))
            if ind > 0:
                max_delta = max(max_delta, abs(num1 - num2) - abs(slist[ind - 1] - num2))
        return (sum_delta - max_delta) % (10 ** 9 + 7)