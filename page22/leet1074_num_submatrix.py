from typing import List

from collections import defaultdict
class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def count_sub(total):
            counter = defaultdict(lambda: 0)
            counter[0] += 1
            ans, p = 0, 0
            for t in total:
                p += t
                if p - target in counter:
                    ans += counter[p - target]
                counter[p] += 1
            return ans

        N = len(matrix)
        M = len(matrix[0])

        ans = 0
        for i in range(N):
            total = [0] * M
            for j in range(i, N):
                for k in range(M):
                    total += matrix[j][k]
                ans += count_sub(total)
        return ans