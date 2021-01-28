from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        sub = [0]
        for num in nums:
            sub.append(sub[-1] + num)
        f = [[10 ** 18] * (m + 1) for _ in range(len(nums) + 1)]
        f[0][0] = 0
        for i in range(1, len(nums) + 1):
            for j in range(1, min(i, m) + 1):
                for k in range(i):
                    f[i][j] = min(f[i][j], max(f[k][j-1], sub[i] - sub[k]))
        return f[len(nums)][m]