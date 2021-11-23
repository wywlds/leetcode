from functools import cache
from typing import List


class Solution:
    def maxHappyGroups(self, B: int, groups: List[int]) -> int:
        groups = [e % B for e in groups]
        remain = [0] * B
        for e in groups:
            remain[e] += 1

        remain = tuple(remain)

        @cache
        def dfs(s, remain):
            ans = 0
            happy = s == 0
            for i in range(len(remain)):
                if remain[i] == 0: continue
                remain2 = list(remain)
                remain2[i] -= 1
                remain2 = tuple(remain2)
                ans = max(ans, happy + dfs((s + i + 1) % B, remain2))
            return ans
        dfs.cache_clear()
        return remain[0] + dfs(0, remain[1:])