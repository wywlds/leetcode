from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()
        waiting_set = set()
        visited_set = set()

        pair_cnt = 0
        for num in nums:
            if num in waiting_set and num not in visited_set:
                pair_cnt += 1
                visited_set.add(num)
            waiting_set.add(num + k)
        return pair_cnt