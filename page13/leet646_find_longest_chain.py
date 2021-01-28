from typing import List

import operator
class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=operator.itemgetter(1))
        num = 0
        last_max = pairs[0][0]-1
        for pair in pairs:
            if pair[0] > last_max:
                num += 1
                last_max = pair[1]
        return num