from typing import List


class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if len(A) < 3 or A[1] <= A[0]:
            return False
        increasing = True
        for i in range(1, len(A) - 1):
            if A[i + 1] == A[i]:
                return False
            if not increasing and A[i + 1] > A[i]:
                return False
            if increasing and A[i + 1] < A[i]:
                increasing = False
        return not increasing