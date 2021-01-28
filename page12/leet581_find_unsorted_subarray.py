from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return 0
        sorted_index = self.find_sorted_index(nums)
        inverse_sorted_index = self.find_sorted_index([-num for num in nums[::-1]])
        inverse_sorted_index = len(nums) - 1 - inverse_sorted_index
        if inverse_sorted_index <= sorted_index + 1:
            return 0
        else:
            return inverse_sorted_index - sorted_index - 1


    def find_sorted_index(self, nums):
        N = len(nums)
        first_i = N - 1
        for i in range(N - 1):
            num1 = nums[i]
            num2 = nums[i + 1]
            if num1 > num2:
                first_i = i
                break
        if first_i == 0:
            return -1
        index = first_i - 1
        for i in range(first_i + 1, N):
            while index >= 0 and nums[index] > nums[i]:
                index -= 1
        return index


if __name__=="__main__":
    solution = Solution()
    print(solution.findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
    print(solution.findUnsortedSubarray([]))
    print(solution.findUnsortedSubarray([1]))



