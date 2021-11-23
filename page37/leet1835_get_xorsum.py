from typing import List


class Solution:
    def getXORSum(self, arr1: List[int], arr2: List[int]) -> int:
        counts1 = [0] * 32
        for a in arr1:
            for i in range(32):
                counts1[i] += 1 & (a >> i)
        counts2 = [0] * 32
        for a in arr2:
            for i in range(32):
                counts2[i] += 1 & (a >> i)

        ans = 0
        for i in range(32):
            if counts2[i] * counts1[i] % 2 == 1:
                ans |= (1 << i)
        return ans