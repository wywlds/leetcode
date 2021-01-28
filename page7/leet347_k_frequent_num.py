from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        most_commons = counter.most_common(k)
        return [most_common[0] for most_common in most_commons]


if __name__=="__main__":
    solution = Solution()
    print(solution.topKFrequent([1,1,1,2,2,3], 2))