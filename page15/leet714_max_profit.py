from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        holding_value, soldout_value = -prices[0], 0
        for p in prices[1:]:
            holding_value = max(holding_value, soldout_value - p)
            soldout_value = max(soldout_value, holding_value + p - fee)
        return soldout_value


if __name__=="__main__":
    solution = Solution()
    print(solution.maxProfit([1, 3, 2, 8, 4, 9], 2))