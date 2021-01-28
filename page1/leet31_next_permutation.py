from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def switch(l, r):
            if l > r:
                return
            tmp = nums[l]
            nums[l] = nums[r]
            nums[r] = tmp
        l = -1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i - 1]:
                l = i
                break

        if l != -1:
            r = -1
            for i in range(len(nums) - 1, -1, -1):
                if nums[l] < nums[i]:
                    r = i
                    break
            switch(l, r)

        r = len(nums)
        while l < r:
            l += 1
            r -= 1
            switch(l, r)


if __name__=="__main__":
    solution = Solution()
    solution.nextPermutation([1,3,2])

