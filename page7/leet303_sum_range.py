from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        self.sums = [0]
        sum = 0
        for num in nums:
            sum += num
            self.sums.append(sum)


    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]