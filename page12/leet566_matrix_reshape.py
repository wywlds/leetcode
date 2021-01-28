from typing import List


class Solution:
    def matrixReshape(self, nums: List[List[int]], r: int, c: int) -> List[List[int]]:
        o_r = len(nums)
        o_c = len(nums[0])
        if o_r * o_c != r * c:
            return nums

        new_m = [[0] * c for _ in range(r)]
        for i in range(o_r):
            for j in range(o_c):
                ind = i * o_c + j
                n_r = ind // c
                n_c = ind % c
                new_m[n_r][n_c] = nums[i][j]

        return new_m


if __name__=="__main__":
    solution = Solution()
