from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        N = len(A)
        left = [0] * N
        right = [0] * N
        for i in range(1, N):
            if A[i] > A[i-1]:
                left[i] = left[i-1] + 1
        for i in range(N-2, -1):
            if A[i] > A[i+1]:
                right[i] = right[i+1] + 1
        ans = 0
        for i in range(N):
            if left[i] > 0 and right[i] > 0:
                ans = max(ans, left[i]+right[i] + 1)

        return ans