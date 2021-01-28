from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        N = len(prices) // 2
        buys, sells = [-10000] * (N + 1), [-1] * (N + 1)
        buys[1] = -prices[0]
        sells[0] = 0
        for price in prices[1:]:
            i = 1
            while i < k + 1 and i < N + 1 and sells[i-1] > -1:
                buys[i] = max(buys[i], sells[i-1] - price)
                sells[i] = max(sells[i], buys[i] + price)
                i += 1
        return max(sells[:k + 1])


if __name__=="__main__":
    solution = Solution()
    print(solution.maxProfit(2, [3,2,6,5,0,3]))