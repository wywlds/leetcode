from typing import List


class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        ans = [0] * len(queries)
        for x, y in points:
            for i, (centerx, centery, radius) in enumerate(queries):
                if (x - centerx) ** 2 + (y - centery) ** 2 <= radius ** 2:
                    ans[i] += 1
        return ans