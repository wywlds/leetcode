from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        for i, num in enumerate(nums):
            if num % n == 0:
                nums[i] = 1001
        ID = 1002
        for i, num in enumerate(nums):
            if num > 1000:
                continue
            j = i
            if num > 0:
                while nums[j] > 0 and nums[j] <= 1000:
                    nums[j], j = ID, (nums[j] + j) % n
            else:
                while nums[j] < 0:
                    nums[j], j = ID, (nums[j] + j) % n
            if nums[j] == ID:
                return True
            ID += 1
        return False


if __name__=="__main__":
    solution = Solution()
    print(solution.circularArrayLoop([-1, 2]))