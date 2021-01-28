from typing import List


from scipy.signal import convolve2d
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return int(abs(convolve2d(grid,[[-2,1],[1,0]])).sum())