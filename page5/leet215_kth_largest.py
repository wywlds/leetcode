from typing import List

import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        m_nums = [-num for num in nums]
        LEN = len(nums)
        if k > LEN / 2:
            return -self.findKthLargest(m_nums, LEN-k)
        heapq.heapify(m_nums)
        for i in range(0, k):
            poped = heapq.heappop(m_nums)
        return -poped


if __name__=="__main__":
    solution = Solution()
    print(solution.findKthLargest([3,2,1,5,6,4], 2))
    print(solution.findKthLargest([3,2,1,5,6,4], 4))
    print(solution.findKthLargest([3,2,3,1,2,4,5,5,6], 4))