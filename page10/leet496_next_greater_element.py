from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0:
            return []

        next_greater_num = {}
        next_greater_num[nums2[len(nums2) - 1]] = -1

        p2 = len(nums2) - 1
        p1 = len(nums2) - 2
        while p1 >= 0:
            value1, value2 = nums2[p1], nums2[p2]
            while True :
                if value2 > value1 or value2 == -1:
                    next_greater_num[value1] = value2
                    break
                else:
                    value2 = next_greater_num[value2]
            p1, p2 = p1-1, p1

        return [next_greater_num[value] for value in nums1]


