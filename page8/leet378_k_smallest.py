from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                #这里的设计也很关键
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left = matrix[0][0]
        right = matrix[n-1][n-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                # 这里的设计很关键
                left = mid + 1
        return right