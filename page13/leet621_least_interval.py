from typing import List

import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = [0] * 26
        for task in tasks:
            counter[ord(task) - ord('A')] += 1
        pq = []
        for num in counter:
            if num != 0:
                pq.append(-num)
        heapq.heapify(pq)
        time = 0
        while pq:
            newq = []
            i = 0
            while i <= n:
                if pq:
                    if pq[0] < -1:
                        newq.append(pq[0] + 1)
                    heapq.heappop(pq)
                time += 1
                if not pq and not newq:
                    break
                i += 1
            for newp in newq:
                heapq.heappush(pq, newp)
        return time