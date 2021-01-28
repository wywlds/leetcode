from typing import List

from operator import truediv, mul, add, sub
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    B = [nums[k] for k in range(len(nums)) if i != k != j]
                    for op in (truediv, mul, add, sub):
                        if j > i and op in (mul, add):
                            continue
                        if op != truediv or nums[j] != 0:
                            result = op(nums[i], nums[j])
                            B.append(result)
                            if self.judgePoint24(B):
                                return True
                            B.pop()
        return False

if __name__=="__main__":
    solution = Solution()
    print(solution.judgePoint24([1,2,1,2]))