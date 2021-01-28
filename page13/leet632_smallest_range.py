from typing import List


import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = []
        K = len(nums)
        max_value = 0

        for i in range(K):
            heapq.heappush(pq, (nums[i][0], i, 0))
            max_value = max(max_value, nums[i][0])
        result = [pq[0][0], max_value]
        while True:
            _, i, j = heapq.heappop(pq)
            if j < len(nums[i]) - 1:
                next_value = nums[i][j + 1]
                j = j + 1
                heapq.heappush(pq, (next_value, i, j))
                max_value = max(next_value, max_value)
                if (max_value - pq[0][0]) < (result[1] - result[0]):
                    result = [pq[0][0], max_value]
            else:
                break
        return result

if __name__=="__main__":
    solution = Solution()
    print(solution.smallestRange([[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]))