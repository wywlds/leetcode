from typing import List

import math
class Solution:
    def countDifferentSubsequenceGCDs(self, nums: List[int]) -> int:
        nums = set(nums)
        c = max(nums)
        ans = 0

        for y in range(1, c + 1):
            g = None
            for x in range(y, c + 1, y):
                if x in nums:
                    if g is None:
                        g = x
                    else:
                        g = math.gcd(g, x)
                    if g == y:
                        ans += 1
                        break
        return ans