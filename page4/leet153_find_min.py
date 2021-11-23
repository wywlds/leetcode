from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] < nums[(m + 1) % len(nums)] and nums[m] < nums[m - 1]:
                return nums[m]
            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
        return nums[l]


if __name__=="__main__":
    nums = [3, 4, 0]
    print(Solution().findMin(nums))