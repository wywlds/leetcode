from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        def get_mins(tstr):
            tstrs = tstr.split(":")
            hour = int(tstrs[0])
            min = int(tstrs[1])
            mins = hour * 60 + min
            return mins

        min_gap = 24 * 60
        for i, tstr in enumerate(timePoints):
            if i == 0:
                gap = get_mins(tstr) + 24 * 60 - get_mins(timePoints[-1])
            else:
                gap = get_mins(tstr) - get_mins(timePoints[i - 1])
            min_gap = min(min_gap, gap)
        return min_gap