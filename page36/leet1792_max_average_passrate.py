from typing import List

import heapq
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        ratios = []
        for p, t in classes:
            ratios.append((- (t-p)/(t * (t + 1)), p/t, p, t))
        heapq.heapify(ratios)
        for i in range(extraStudents):
            _, r, p, t = heapq.heappop(ratios)
            p += 1
            t += 1
            r = p / t
            heapq.heappush(ratios, (- (t-p)/(t * (t + 1)), r, p, t))
        return sum([ratio[1] for ratio in ratios]) / len(classes)