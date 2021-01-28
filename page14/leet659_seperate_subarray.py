from typing import List

import collections
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counts = collections.Counter(nums)
        tails = collections.Counter()
        for num in nums:
            if counts[num] == 0:
                continue
            elif tails[num] > 0:
                tails[num] -= 1
                tails[num+1] += 1
            elif counts[num + 1] > 0 and counts[num + 2] > 0:
                counts[num + 1] -= 1
                counts[num + 2] -= 1
                tails[num + 3] += 1
            else:
                return False
            counts[num] -= 1
        return True
