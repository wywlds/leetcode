from typing import List
from operator import itemgetter


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        ans = [2*T] * (T+1)
        ans[0] = 0
        clips.sort(key=itemgetter(1))
        for start, end in clips:
            base = ans[start]
            for i in range(start+1, end+1):
                ans[i] = min(base + 1, ans[i])

        if ans[T] == 2 * T:
            return -1
        else:
            return ans[T]