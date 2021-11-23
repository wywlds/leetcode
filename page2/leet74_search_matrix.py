from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        pivots = [m[0] for m in matrix]
        import bisect
        x = bisect.bisect_left(pivots, target)
        if x < len(pivots) and pivots[x] == target:
            return True
        if x == 0:
            return False
        y = bisect.bisect_left(matrix[x - 1], target)
        return y < len(matrix[x-1]) and matrix[x - 1][y] == target


if __name__=="__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    solution = Solution()
    for i in range(70):
        print("%d-%s" % (i, solution.searchMatrix(matrix, i)))
