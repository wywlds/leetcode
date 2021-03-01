from typing import List

import bisect
class Solution:
    def closestCost(self, baseCosts: List[int], toppingCosts: List[int], target: int) -> int:
        topping_combs = []
        for i in range(3 ** len(toppingCosts)):
            cost = 0
            j = 0
            while i != 0:
                if i % 3 == 1:
                    cost += toppingCosts[j]
                elif i % 3 == 2:
                    cost += 2 * toppingCosts[j]
                i = i // 3
                j += 1
            topping_combs.append(cost)
        max_delta = float('inf')
        ans = 0
        topping_combs.sort()
        for base_cost in baseCosts:
            delta = target - base_cost
            bi = bisect.bisect_left(topping_combs, delta)
            deltas = [topping_combs[bi]]
            if bi > 0:
                deltas.append(topping_combs[bi-1])
            for delta in deltas:
                if abs(target - base_cost - delta) < max_delta or (abs(target - base_cost - delta) == max_delta and (
                        base_cost + delta) < ans):
                    ans = base_cost + delta
                    max_delta = abs(target - base_cost - delta)
        return ans

if __name__=="__main__":
    baseCosts = [2,3]
    toppingCosts = [4,5,100]
    target = 18
    solution = Solution()
    print(solution.closestCost(baseCosts, toppingCosts, target))