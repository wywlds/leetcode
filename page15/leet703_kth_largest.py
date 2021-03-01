from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.larger_heap = [float('-inf')]*k
        for num in nums:
            self.add(num)


    def add(self, val: int) -> int:
        if val > self.larger_heap[0]:
            heapq.heappop(self.larger_heap)
            heapq.heappush(self.larger_heap, val)
        return self.larger_heap[0]


if __name__=="__main__":
    kthLargest = KthLargest(3, [4, 5, 8, 2])
    print(kthLargest.add(3))