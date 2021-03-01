from typing import List

import heapq
import math
class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        lo = 1
        hi = max(nums)
        while lo <= hi:
            mid = (lo + hi) // 2
            cnt = 0
            for num in nums:
                cnt += (num - 1) // mid
            if cnt <= maxOperations:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

if __name__=="__main__":
    nums = [2,4,8,2]
    maxOperations = 4
    solution = Solution()
    print(solution.minimumSize(nums, maxOperations))