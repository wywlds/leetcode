from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        start = 0
        ans = 0
        for i, num in enumerate(nums):
            if num != nums[start]:
                if nums[start] == 1:
                    ans = max(ans, i - start)
                start = i
        if nums[start] == 1:
            ans = max(ans, len(nums) - start)
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.findMaxConsecutiveOnes([1,0,1,1,0,1]))