from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) == 0:
            return []
        greater_dict = {}
        dec_stack = []
        for i in range(len(nums2)):
            value = nums2[i]
            while dec_stack and dec_stack[-1] < value:
                greater_dict[dec_stack.pop()] = value
            dec_stack.append(value)
        for value in dec_stack:
            greater_dict[value] = -1
        return [greater_dict[num] for num in nums1]



