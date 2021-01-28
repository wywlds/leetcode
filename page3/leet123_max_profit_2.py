from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy1, sell1, buy2, sell2 = float('-inf'), float('-inf'), float('-inf'), float('-inf')
        for price in prices:
            buy1, sell1, buy2, sell2 = max(buy1, 0 - price), max(sell1, buy1 + price), max(buy2, sell1 - price), \
                                       max(sell2, buy2 + price)
        return sell2