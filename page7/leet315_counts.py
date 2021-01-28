from typing import List


import bisect
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sort_array = []
        counts = [0] * len(nums)
        LEN = len(nums)
        for i, num in enumerate(nums[::-1]):
            ind = bisect.bisect_left(sort_array, num)
            sort_array.insert(ind, num)
            counts[LEN - 1 -i] = ind
        return counts
