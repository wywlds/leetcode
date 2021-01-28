from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        residu_map = {}
        for i, num in enumerate(numbers):
            if num in residu_map:
                return [residu_map[num], i]
            residu_map[target - num] = i
        return []