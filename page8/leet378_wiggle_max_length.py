from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        prediff = nums[1] - nums[2]
        if prediff == 0:
            ans = 1
        else:
            ans = 2
        for i in range(1, len(nums) - 1):
            cur_diff = nums[i + 1] - nums[i]
            if cur_diff < 0 and prediff >= 0:
                ans += 1
                prediff = cur_diff
            elif cur_diff >0 and prediff <= 0:
                ans += 1
                prediff = cur_diff
        return ans

    def wiggleMaxLength2(self, nums: List[int]) -> int:
        up, down = 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                down = up + 1
            elif nums[i] < nums[i - 1]:
                up = down + 1
        return max(up, down)
