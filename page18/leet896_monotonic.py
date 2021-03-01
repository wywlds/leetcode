from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        def isMonoIncreasing(A):
            for i in range(len(A) - 1):
                if A[i + 1] < A[i]:
                    return False
            return True

        return isMonoIncreasing(A) or isMonoIncreasing(A[::-1])