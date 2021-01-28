from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        N = len(nums)
        k = k % N
        self.inner_rotate(nums, 0, N - 1)
        self.inner_rotate(nums, 0, k - 1)
        self.inner_rotate(nums, k, N - 1)

    def inner_rotate(self, nums, start, end):
        while start < end:
            tmp = nums[end]
            nums[end] = nums[start]
            nums[start] = tmp
            start += 1
            end -= 1


if __name__=="__main__":
    solution = Solution()
    nums = [1,2,3,4,5,6,7,8]
    solution.rotate(nums, 3)
    print(nums)