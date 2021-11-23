from functools import lru_cache
from typing import List
import bisect

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        max_len = 0
        ans = []
        @lru_cache(None)
        def dfs(j):
            max_len = 1
            ans = [nums[j]]
            for k in range(j + 1, len(nums)):
                if nums[k] % nums[j] == 0:
                    c, l = dfs(k)
                    if c + 1 > max_len:
                        max_len = c + 1
                        ans = [nums[j]] + l
            return max_len, ans

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] % nums[i] == 0:
                    c, l = dfs(j)
                    if c + 1 > max_len:
                        ans = [nums[i]] + l
                        max_len = c + 1
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.largestDivisibleSubset([2,3,4,6,9,27]))