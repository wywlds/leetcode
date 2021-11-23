from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        ans = []
        ans.append(first)
        for encode in encoded:
            ans.append(encode ^ ans[-1])
        return ans
