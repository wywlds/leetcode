from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        left_nums = [0]
        right_nums = [0]
        mid = len(nums) // 2
        for num in nums[:mid + 1]:
            LEFT_N = len(left_nums)
            for j in range(LEFT_N):
                left_nums.append(left_nums[j] + num)

        for num in nums[mid+1:]:
            RIGHT_N = len(right_nums)
            for j in range(RIGHT_N):
                right_nums.append(right_nums[j] + num)

        left_nums.sort()
        right_nums.sort(reverse=True)
        i, j = 0, 0
        ans = float('inf')
        while i < len(left_nums) and j < len(right_nums):
            ans = min(ans, abs(left_nums[i] + right_nums[j] - goal))
            if ans == 0:
                return 0
            if left_nums[i] + right_nums[j] > goal:
                j += 1
            else:
                i += 1
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.minAbsDifference([7,-9,15,-2], -5))