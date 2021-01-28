from typing import List

import functools
import heapq
class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=functools.cmp_to_key(lambda x, y : x[1] - y[1]))
        pq = []
        d = 0
        for i, (c_dur, c_d) in enumerate(courses):
            if i == 0:
                pq = [-c_dur]
                d = c_dur
            else:
                if d + c_dur > c_d:
                    if -pq[0] > c_dur:
                        poped = -pq[0]
                        heapq.heappop(pq)
                        heapq.heappush(pq, -c_dur)
                        d = d + poped + c_dur
                else:
                    heapq.heappush(pq, -c_dur)
                    d += c_dur
        return len(pq)


if __name__=="__main__":
    solution = Solution()
    print(solution.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))