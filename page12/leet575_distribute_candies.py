from typing import List


class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
        different_species = len(set(candies))
        n = len(candies) // 2
        return min(different_species, n)