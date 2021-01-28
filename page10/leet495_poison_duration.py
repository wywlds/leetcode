from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if len(timeSeries) == 0:
            return 0
        p1 = 0
        p2 = 1
        total_duration = 0
        while p1 != len(timeSeries) - 1:
            time1 = timeSeries[p1]
            time2 = timeSeries[p2]
            delta_time = time2 - time1
            if delta_time < duration:
                total_duration += delta_time
            else:
                total_duration += duration
            p1 += 1
            p2 += 1
        total_duration += duration
        return total_duration