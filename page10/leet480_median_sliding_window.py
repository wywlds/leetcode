from typing import List

from collections import defaultdict
import heapq
class DualHeap:
    def __init__(self, k):
        self.small = []
        self.large = []
        self.delayed = defaultdict(lambda: 0)

        self.k = k
        self.small_size = 0
        self.large_size = 0

    def prune(self, heap):
        while heap:
            num = heap[0]
            if heap is self.small:
                num = -num
            if num in self.delayed and self.delayed[num] > 0:
                self.delayed[num] -= 1
                heapq.heappop(heap)
            else:
                break

    def make_balance(self):
        if self.small_size > self.large_size + 1:
            heapq.heappush(self.large, - self.small[0])
            heapq.heappop(self.small)
            self.small_size -= 1
            self.large_size += 1
            self.prune(self.small)
        elif self.small_size < self.large_size:
            heapq.heappush(self.small, - self.large[0])
            heapq.heappop(self.large)
            self.small_size += 1
            self.large_size -= 1
            self.prune(self.large)

    def insert(self, num):
        if not self.small or num < -self.small[0]:
            heapq.heappush(self.small, - num)
            self.small_size += 1
        else:
            heapq.heappush(self.large, num)
            self.large_size += 1
        self.make_balance()

    def erase(self, num):
        self.delayed[num] += 1
        if num <= -self.small[0]:
            self.small_size -= 1
            if num == -self.small[0]:
                self.prune(self.small)
        else:
            self.large_size -= 1
            if num == self.large[0]:
                self.prune(self.large)
        self.make_balance()

    def get_median(self):
        return float(-self.small[0]) if self.k % 2 == 1 else (-self.small[0] + self.large[0]) / 2



class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        dual_h = DualHeap(k)
        ans = []
        for i, num in enumerate(nums):
            dual_h.insert(num)
            if i >= k:
                dual_h.erase(nums[i-k])
                ans.append(dual_h.get_median())
            elif i == k - 1:
                ans.append(dual_h.get_median())
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.medianSlidingWindow([1,3,-1,-3,5,3,6,7], 4))