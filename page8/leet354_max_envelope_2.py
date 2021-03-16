from typing import List

import bisect
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        if not envelopes:
            return 0

        n = len(envelopes)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        q = [envelopes[0][1]]
        for i in range(1, len(envelopes)):
            cur_right = envelopes[i][-1]
            if cur_right > q[-1]:
                q.append(cur_right)
            else:
                index = bisect.bisect_left(q, cur_right)
                q[index] = cur_right
        return len(q)

if __name__=="__main__":
    enveloppes = [[5,4],[6,4],[6,7],[2,3]]
    solution = Solution()
    print(solution.maxEnvelopes(enveloppes))