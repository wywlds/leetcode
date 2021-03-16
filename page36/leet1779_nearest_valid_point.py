from typing import List


class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        ans = -1
        max_d = float('inf')
        for i, (a, b) in  enumerate(points):
            if a != x and b != y:
                continue
            if a == x:
                d = abs(y - b)
                if d < max_d:
                    ans = i
                    max_d = d
            elif b == y:
                a = abs(x - a)
                if d < max_d:
                    ans = i
                    max_d = d
        return ans