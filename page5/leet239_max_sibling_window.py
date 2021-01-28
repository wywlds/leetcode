from typing import List

import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 0:
            return []
        q = [(-num, i) for i, num in enumerate(nums[:k])]
        heapq.heapify(q)
        ans = []
        ans.append(-q[0][0])
        for i in range(k, len(nums)):
            num = nums[i]
            heapq.heappush(q, (-num, i))
            while True:
                top_num, top_i = q[0]
                if top_i > i - k:
                    ans.append(-top_num)
                    break
                else:
                    heapq.heappop(q)
        return ans


if __name__=="__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    solution = Solution()
    print(solution.maxSlidingWindow(nums, k))