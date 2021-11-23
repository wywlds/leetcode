from typing import List

import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        task_q = []
        for i, (enq_t, p_t) in enumerate(tasks):
            task_q.append((p_t, i, enq_t))
        task_q.sort(key=lambda tup: tup[2])
        h = []
        i = 0
        cur_time = float('-inf')

        ans = []
        while len(h) != 0 or i < len(task_q):
            if len(h) == 0:
                cur_time = task_q[i][2]
            else:
                p_t, ind, _ = heapq.heappop(h)
                cur_time += p_t
                ans.append(ind)
            while i < len(task_q) and task_q[i][2] <= cur_time:
                heapq.heappush(h, task_q[i])
                i += 1
        return ans