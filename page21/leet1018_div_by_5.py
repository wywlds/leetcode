from typing import List


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        ans = []
        residu = 0
        for a in A:
            residu = (residu * 2 + a) % 5
            ans.append(residu == 0)
        return ans