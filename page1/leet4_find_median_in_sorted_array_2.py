from typing import List
import math
import numpy as np


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total_len = len(nums1) + len(nums2) + 1
        l_index = math.floor(total_len / 2)
        r_index = math.ceil(total_len / 2)
        l_value = self.findK(nums1, nums2, l_index)
        r_value = self.findK(nums1, nums2, r_index)
        return (l_value + r_value) / 2

    def findK(self, nums1, nums2, ind):
        if len(nums1) < len(nums2):
            return self.findK(nums2, nums1, ind)
        if len(nums2) == 0:
            return nums1[ind - 1]
        if ind == 1:
            return nums1[0] if nums1[0] < nums2[0] else nums2[0]
        k = min(math.floor(ind / 2), len(nums2))
        if nums1[k - 1] < nums2[k - 1]:
            return self.findK(nums1[k:], nums2, ind - k)
        else:
            return self.findK(nums1, nums2[k:], ind - k)

if __name__=="__main__":
    solution = Solution()

    result = solution.findMedianSortedArrays([1,3], [2])
    print(result)
    result = solution.findMedianSortedArrays([1,2,3], [4,5,6])

    print(result)
    import numpy as np
    randlist = np.random.randint(0, high=100, size=10)
    randlist2 = np.random.randint(0, high=100, size=12)
    randlist.sort()
    randlist2.sort()
    median = solution.findMedianSortedArrays(randlist, randlist2)

    new_list = np.concatenate([randlist, randlist2])
    new_list.sort()
    new_median = np.median(new_list)
    print(median)
    print(new_median)
    pass