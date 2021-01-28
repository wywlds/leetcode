from typing import List
from collections import defaultdict


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        counter1 = defaultdict(lambda : 0)
        counter2 = defaultdict(lambda : 0)
        for a in A:
            for b in B:
                counter1[a + b] += 1
        for c in C:
            for d in D:
                counter2[c + d] += 1

        ans = 0
        for s, c in counter1.items():
            if -s in counter2:
                ans += c * counter2[-s]
        return ans