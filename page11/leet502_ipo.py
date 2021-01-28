from typing import List
import heapq


class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        capital_heap = list(zip(Capital, Profits))
        heapq.heapify(capital_heap)
        profit_heap = []
        for i in range(k):
            while capital_heap and capital_heap[0][0] <= W:
                capital, profit = heapq.heappop(capital_heap)
                heapq.heappush(profit_heap, -profit)
            if not profit_heap:
                break
            W -= heapq.heappop(profit_heap)
        return W


if __name__=="__main__":
    k = 2
    W = 0
    profits = [1, 2, 3]
    capitals = [0, 1, 1]

    solution = Solution()
    print(solution.findMaximizedCapital(k, W, profits, capitals))