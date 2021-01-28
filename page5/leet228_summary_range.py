from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        start = nums[0]
        ans = []
        for i, num in enumerate(nums[1:]):
            if num != nums[i] + 1:
                if nums[i] != start:
                    ans.append("{}->{}".format(start, nums[i]))
                else:
                    ans.append(start)
                start = num
        if nums[-1] != start:
            ans.append("{}->{}".format(start, nums[-1]))
        else:
            ans.append(str(start))
        return ans
