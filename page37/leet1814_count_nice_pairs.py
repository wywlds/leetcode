from typing import List

from collections import defaultdict
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def delta(x):
            rev = 0
            tmp = x
            while tmp != 0:
                cur = tmp % 10
                tmp = tmp // 10
                rev = rev * 10 + cur
            return x - rev

        counter = defaultdict(lambda: 0)
        for num in nums:
            d = delta(num)
            counter[d] += 1

        ans = 0
        BASE = 10 ** 9 + 7
        for _, cnt in counter.items():
            ans = (ans + cnt * (cnt - 1) // 2) % BASE

        return ans