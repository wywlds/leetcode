from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        dec_stack = []
        larger_value = [-1] * len(nums)
        for i in range(2*len(nums)):
            ind = i % len(nums)
            while dec_stack and nums[dec_stack[-1]] < nums[ind]:
                smaller_index = dec_stack.pop()
                larger_value[smaller_index] = nums[ind]
            dec_stack.append(ind)
        return larger_value


if __name__=="__main__":
    solution = Solution()
    print(solution.nextGreaterElements([1,2,1]))
    print(solution.nextGreaterElements([]))
    print(solution.nextGreaterElements([1,1,1]))
    print(solution.nextGreaterElements([1,2,3,2,1]))