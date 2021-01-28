from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        left = self.binary_search(nums, target, True)
        right = self.binary_search(nums, target, False) - 1
        if left <= right and right != len(nums) and nums[left] == target and nums[right] == target:
            return [left, right]
        return [-1, -1]

    def binary_search(self, nums, target, lower):
        left, right = 0, len(nums) - 1
        ans = len(nums)
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target or (nums[mid] >= target and lower):
                right = mid - 1
                ans = mid
            else:
                left = mid + 1
        return ans
