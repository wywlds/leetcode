from typing import List


import bisect
class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        count = 0
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                max_len = nums[i] + nums[j]
                index = bisect.bisect_left(nums[j+1:], max_len)
                count += index
        return count

if __name__=="__main__":
    solution = Solution()
    print(solution.triangleNumber([3,2,2,4]))