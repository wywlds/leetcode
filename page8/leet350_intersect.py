from typing import List

import collections
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        k1 = set(counter1.keys())
        k2 = set(counter2.keys())
        ik = k1.intersection(k2)
        result = []
        for k in ik:
            count = min(counter1[k], counter2[k])
            result.extend([k] * count)
        return result