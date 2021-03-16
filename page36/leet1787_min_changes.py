from typing import List

from collections import defaultdict
class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        INF = 0x3f3f3f3f
        size = [0] * k
        counts = [defaultdict(lambda: 0) for _ in range(k)]

        N = len(nums)
        for i in range(k):
            j = 0
            while i + j < N:
                size[i] += 1
                counts[i][nums[i + j]] += 1
                j += k

        dp = [INF] * (2 ** 10)
        dp[0] = 0
        for i in range(k):
            min_l = min(dp)
            ndp = [min_l + size[i]] * (2 ** 10)
            for q, c in counts[i].items():
                if i == 0:
                    v = q ^ 0
                    ndp[v] = min(ndp[v], dp[0] + size[i] - c)
                else:
                    for j in range(2 ** 10):
                        v = q ^ j
                        ndp[v] = min(ndp[v], dp[j] + size[i] - c)
            dp = ndp
        return dp[0]

if __name__=="__main__":
    nums = [3,4,5,2,1,7,3,4,7]
    k = 3
    solution = Solution()
    print(solution.minChanges(nums, k))