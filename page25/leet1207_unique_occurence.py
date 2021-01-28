from collections import Counter
from typing import List


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        cnts = counter.values()
        return len(cnts) == len(set(cnts))


if __name__=="__main__":
    a = [-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]
    solution = Solution()
    print(solution.uniqueOccurrences(a))