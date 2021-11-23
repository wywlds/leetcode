from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        state1 = [-1, 0]
        for num in nums[1:]:
            last_state0 = state1[0]
            state1[0] = state1[1] + num
            state1[1] = max(last_state0, state1[1])

        state2 = [-1, nums[0]]
        for num in nums[2:len(nums) - 1]:
            last_state0 = state2[0]
            state2[0] = state2[1] + num
            state2[1] = max(state2[1], last_state0)
        return max(max(state1), max(state2))

if __name__=="__main__":
    solution = Solution()
    print(solution.rob([200,3,140,20,10]))