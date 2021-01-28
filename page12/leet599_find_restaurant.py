from typing import List

import heapq
class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        q = []
        for i, res1 in enumerate(list1):
            for j, res2 in enumerate(list2):
                if res1 == res2:
                    heapq.heappush(q, (i+j, res1))
        min_index = q[0][0]
        results =[]
        while q and q[0][0] == min_index:
            _, res = heapq.heappop(q)
            results.append(res)
        return results