from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        LEN = len(nums)
        for i in range(LEN):
            sum_r = nums[i]
            for j in range(i+1, LEN):
                sum_r = sum_r + nums[j]
                if  (sum_r == 0 and k == 0) or (k != 0 and sum_r % k == 0):
                    return True
        return False

if __name__=="__main__":
    solution = Solution()
    print(solution.checkSubarraySum([23,2,6,4,7], 6))