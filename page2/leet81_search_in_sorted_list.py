from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums) - 1
        if len(nums) == 1:
            return nums[0] == target

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return True

            ## 关键是要在 左==中==右 的时候移动到可以判断
            if nums[l] == nums[m] and nums[r] == nums[m]:
                l += 1
                r -= 1
            elif nums[l] <= nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            else:
                if nums[m] <= target <= nums[r]:
                    l = m + 1
                else:
                    r = m - 1
        return False