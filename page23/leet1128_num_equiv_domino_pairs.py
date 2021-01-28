from typing import List
from collections import defaultdict


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        dic = defaultdict(lambda : 0)
        ans = 0
        for a, b in dominoes:
            if a < b:
                tup = (a, b)
            else:
                tup = (b, a)
            ans += dic[tup]
            dic[tup] += 1
        return ans