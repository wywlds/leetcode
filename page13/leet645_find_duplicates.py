from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        result = [0, 0]
        for i, num in enumerate(nums):
            if nums[abs(num) - 1] < 0:
                result[0] = abs(num)
            else:
                nums[abs(num) - 1] = - nums[abs(num) - 1]
        for i, num in enumerate(nums):
            if num > 0:
                result[1] = i + 1
        return result

if __name__=="__main__":
    solution = Solution()
    #print(solution.findErrorNums([1,2,2,3,4]))
    #print(solution.findErrorNums([3,2,2]))
    #print(solution.findErrorNums([7,4,5,6,3,2,2]))
    print(solution.findErrorNums([3,3,1]))