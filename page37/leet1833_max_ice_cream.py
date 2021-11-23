class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        base = 0
        ans = 0
        i = 0
        while i < len(costs):
            base += costs[i]
            i += 1
            if base <= coins:
                ans += 1
            else:
                break
        return ans