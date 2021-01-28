from typing import List


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        xs = [x for x, _ in ops]
        ys = [y for _, y in ops]
        return (min(xs) + 1) * (min(ys) + 1)