from typing import List


class Solution:
    def getMaximumConsecutive(self, coins: List[int]) -> int:
        coins.sort()
        cur_max = 0
        for coin in coins:
            if coin > cur_max + 1:
                return cur_max + 1
            else:
                cur_max = cur_max + coin
        return cur_max + 1