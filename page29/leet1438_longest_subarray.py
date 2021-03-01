from typing import List

import heapq
class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l, r = 0, 0
        max_h, min_h = [], []
        N = len(nums)
        ans = 1
        while r < N:
            num = nums[r]
            heapq.heappush(max_h, (-num, r))
            heapq.heappush(min_h, (num, r))
            while -max_h[0][0] - min_h[0][0] > limit:
                while l >= max_h[0][1]:
                    heapq.heappop(max_h)
                while l >= min_h[0][1]:
                    heapq.heappop(min_h)
                l += 1
            ans = max(r - l + 1, ans)
            r += 1
        return ans

if __name__=="__main__":
    nums = [4,2,2,2,4,4,2,2]
    limit = 0
    solution = Solution()
    print(solution.longestSubarray(nums, limit))