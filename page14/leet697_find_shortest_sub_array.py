from typing import List

from collections import defaultdict
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = defaultdict(lambda : [0, 0, 0])
        max_count = 0
        max_items = []
        max_index_dic = {}
        for i, num in enumerate(nums):
            if num not in counter:
                counter[num][2] = i
            counter[num][1] = i - counter[num][2] + 1
            counter[num][0] += 1
            if counter[num][0] > max_count:
                max_count = counter[num][0]
                max_items = [counter[num][1:]]
            elif counter[num][0] == max_count:
                max_items.append(counter[num][1:])

        max_items.sort()
        return max_items[0][0]


if __name__=="__main__":
    solution = Solution()
    print(solution.findShortestSubArray([1,2,2,3,1,4,2]))