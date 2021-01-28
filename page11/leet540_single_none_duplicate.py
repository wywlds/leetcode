from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) < 10:
            for i in range(len(nums) - 1):
                num = nums[i]
                if num != nums[i + 1] and num != nums[i - 1]:
                    return num
        i = len(nums) // 2
        if i % 2 == 0:
            if nums[i + 1] != nums[i]:
                return self.singleNonDuplicate(nums[:i+2])
            else:
                return self.singleNonDuplicate(nums[i+2:])
        else:
            if nums[i - 1] != nums[i]:
                return self.singleNonDuplicate(nums[:i+1])
            else:
                return self.singleNonDuplicate(nums[i+1:])


if __name__=="__main__":
    solution = Solution()
    print(solution.singleNonDuplicate([1,1,2,3,3,4,4,8,8,9,9,10,10,11,11,12,12,13,13]))
    print(solution.singleNonDuplicate([1]))
    print(solution.singleNonDuplicate([3,3,7,7,10,11,11,12,12,13,13]))