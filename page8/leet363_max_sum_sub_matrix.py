from typing import List

from sortedcontainers import SortedList


class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        M = len(matrix)
        if M == 0:
            return 0
        N = len(matrix[0])
        if N == 0:
            return 0
        ans = float('-inf')
        for i in range(M):
            agg = [0] * N
            for j in range(i, M):
                for c in range(N):
                    agg[c] += matrix[j][c]

                sset = SortedList([0])
                s = 0
                for a in agg:
                    s += a
                    ind = sset.bisect_left(s - k)
                    if ind != len(sset):
                        cur = s - sset[ind]
                        ans = max(cur, ans)
                    sset.add(s)
        return ans

if __name__=="__main__":
    matrix = [[2,2,-1]]
    k = 3
    print(Solution().maxSumSubmatrix(matrix, k))