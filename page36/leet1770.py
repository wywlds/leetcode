from typing import List

from collections import defaultdict
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        m = len(multipliers)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        for l in range(1, m + 1):
            dp[l][0] = dp[l - 1][0] + nums[l - 1] * multipliers[l - 1]
        for r in range(1, m + 1):
            dp[0][r] = dp[0][r - 1] + nums[-r] * multipliers[r - 1]
        for i, multiplier in enumerate(multipliers):
            num_occupied = i + 1
            for l in range(1, num_occupied + 1):
                r = num_occupied - l
                dp[l][r] = dp[l-1][r] + multiplier * nums[l - 1]
                if r != 0:
                    dp[l][r] = max(dp[l][r], dp[l][r - 1] + multiplier * nums[-r])
        ans = float('-inf')
        for l in range(0, m + 1):
            r = m - l
            ans = max(ans, dp[l][r])
        return ans


if __name__=="__main__":
    nums = [-854,-941,10,299,995,-346,294,-393,351,-76,210,897,-651,920,624,969,-629,985,-695,236,637,-901,-817,546,-69,
      192,-377,251,542,-316,-879,-764,-560,927,629,877,42,381,367,-549,602,139,-312,-281,105,690,-376,-705,-906,85,-608,639,752,770,-139,-601,341,61,969,276,176,-715,-545,471,-170,-126,596,-737,130]
    multipliers = [83,315,-442,-714,461,920,-737,-93,-818,-760,558,-584,-358,-228,-220]
    solution = Solution()
    # 3040819
    print(solution.maximumScore(nums, multipliers))