from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        change_count = [0] * (amount + 1)
        change_count[amount] = 1
        coins.sort(reverse=True)
        for coin in coins:
            for i in range(amount, 0, -1):
                if i - coin >= 0:
                    change_count[i-coin] += change_count[i]
        return change_count[0]


if __name__=="__main__":
    solution = Solution()
    print(solution.change(5, [1,2,5]))
    print(solution.change(3, [2]))
    print(solution.change(10, [10]))