from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        for last_price, this_price in zip(prices[:len(prices) - 1], prices[1:]):
            ans += max(this_price-last_price, 0)
        return ans