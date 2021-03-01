from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        LEN = len(customers)
        unsatisfied_cnt = [0] * (LEN + 1)
        cnt_customer = 0
        max_X = 0
        for i, (customer, grum) in enumerate(zip(customers, grumpy)):
            cnt_customer += (1 - grum)* customer
            unsatisfied_cnt[i + 1] = unsatisfied_cnt[i] + customer * grum
            if i >= X - 1:
                max_X = max(unsatisfied_cnt[i + 1] - unsatisfied_cnt[i - X + 1], max_X)
        return cnt_customer + max_X


if __name__ == "__main__":
    customers = [1,0,1,2,1,1,7,5]
    grumpy = [0,1,0,1,0,1,0,1]
    X = 3
    solution = Solution()
    print(solution.maxSatisfied(customers, grumpy, X))