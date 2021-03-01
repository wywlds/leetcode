from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums) + 1
        for i, num in enumerate(nums):
            num = num % n
            nums[num - 1] += n
        for i, num in enumerate(nums):
            if num <= n:
                ans.append(i + 1)
        return ans

if __name__=="__main__":
    nums = [4,3,2,7,8,2,3,1]
    solution = Solution()
    print(solution.findDisappearedNumbers(nums))