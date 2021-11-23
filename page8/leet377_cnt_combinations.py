from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        mem = [0] * (target + 1)
        mem[target] = 1
        nums.sort()
        for i in range(target, 0, -1):
            for num in nums:
                minused = i - num
                if minused < 0:
                    break
                else:
                    mem[minused] += mem[i]
        return mem[0]