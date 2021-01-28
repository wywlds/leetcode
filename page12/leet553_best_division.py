from typing import List


class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return str(nums[0]) + "/" + str(nums[1])
        result_str = str(nums[0]) + "/("
        result_str += "/".join([str(num) for num in nums[1:]])
        result_str += ")"
        return result_str


if __name__=="__main__":
    solution = Solution()
    print(solution.optimalDivision([1,2,3]))