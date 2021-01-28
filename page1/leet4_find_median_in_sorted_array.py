from typing import List
import math


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            return self.median(nums2, 0, len(nums2) - 1)
        elif len(nums2) == 0:
            return self.median(nums1, 0, len(nums1) - 1)
        elif len(nums1) >= len(nums2):
            return self.findMedianSortedArrays_internal(nums1, nums2)
        else:
            return self.findMedianSortedArrays_internal(nums2, nums1)

    def findMedianSortedArrays_internal(self, long_list, short_list):
        long_start = 0
        long_end = len(long_list) - 1
        short_start = 0
        short_end = len(short_list) - 1
        while short_start != short_end and short_start != (short_end -1):
            median_short = self.median(short_list, short_start, short_end)
            median_long = self.median(long_list, long_start, long_end)
            diff = math.floor((short_end - short_start) / 2)

            if median_short == median_long:
                return median_short
            elif median_short < median_long:
                short_start += diff
                long_end -= diff
            else:
                short_end -= diff
                long_start += diff

        med_i = (long_start + long_end) / 2
        long_sub_list = long_list[max(long_start, math.floor(med_i) - 1): min(long_end+1, math.ceil(med_i) + 2)]
        short_sub_list = short_list[short_start:short_end+1]
        p1 = 0
        p2 = 0
        sorted_list = []
        while len(sorted_list) < len(long_sub_list) + len(short_sub_list):
            if p1 == len(long_sub_list):
                sorted_list.append(short_sub_list[p2])
                p2 += 1
            elif p2 == len(short_sub_list):
                sorted_list.append(long_sub_list[p1])
                p1 += 1
            else:
                if long_sub_list[p1] < short_sub_list[p2]:
                    sorted_list.append(long_sub_list[p1])
                    p1 += 1
                else:
                    sorted_list.append(short_sub_list[p2])
                    p2 += 1
        return self.median(sorted_list, 0, len(sorted_list) - 1)

    def median(self, list, start, end):
        med_i = (start + end) / 2
        return (list[math.floor(med_i)] + list[math.ceil(med_i)]) / 2

if __name__=="__main__":
    solution = Solution()

    # result = solution.findMedianSortedArrays([1,3], [2])
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
    pass