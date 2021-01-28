from typing import List


class Solution:
    def largeGroupPositions(self, s: str) -> List[List[int]]:
        cur, start = "", -1
        ans = []
        for i, ch in enumerate(s):
            if ch == cur:
                continue
            else:
                if i - 1 - start >= 2:
                    ans.append([start, i - 1])
                cur, start = ch, i
        if len(s) - 1 - start >= 2:
            ans.append([start, len(s) - 1])
        return ans