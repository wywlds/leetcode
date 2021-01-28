from typing import List
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1, stone2 = heapq.heappop(stones), heapq.heappop(stones)
            if stone1 == stone2:
                continue
            else:
                heapq.heappush(stone1 - stone2)
        return -stones[0] if len(stones) > 0 else 0