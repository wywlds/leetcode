from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        inserted = False
        ans = []
        for interval in intervals:
            if interval[0] > newInterval[1]:
                if not inserted:
                    ans.append(newInterval)
                    inserted = True
                ans.append(interval)

            elif interval[1] < newInterval[0]:
                ans.append(interval)

            else:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
        if not inserted:
            ans.append(newInterval)
        return ans