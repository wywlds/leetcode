from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f_1 = - prices[0]
        f_2 = 0
        f_3 = 0
        for price in prices[1:]:
            new_f_1 = max(f_1, f_3 - price)
            new_f_2 = f_1 + price
            new_f_3 = max(f_3, f_2)
            f_1 = new_f_1
            f_2 = new_f_2
            f_3 = new_f_3
        return max(f_2, f_3)


if __name__=="__main__":
    solution = Solution()
    print(solution.maxProfit([1,2,3,0,2]))
