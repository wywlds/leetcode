from typing import List


class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        xor_res = 0
        ans = []
        maximum = 2 ** maximumBit - 1
        for num in nums:
            xor_res = xor_res ^ num
            ans.append(xor_res ^ maximum)
        return ans[::-1]