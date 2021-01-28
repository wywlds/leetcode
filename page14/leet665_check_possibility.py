from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        LEN = len(nums)
        count_abnormal = 0
        for i, num in enumerate(nums):
            if i == LEN - 1:
                return True
            if num > nums[i+1]:
                if count_abnormal == 1:
                    return False
                count_abnormal += 1
                if i == 0:
                    pass
                elif nums[i+1] >= nums[i-1]:
                    pass
                elif i==LEN-2 or nums[i + 2] >= num:
                    pass
                else:
                    return False
        return True

if __name__=="__main__":
    solution = Solution()
    print(solution.checkPossibility([4,2,3]))
    print(solution.checkPossibility([1,2,4,5,3]))