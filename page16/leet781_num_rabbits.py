from typing import List

from collections import defaultdict
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = defaultdict(lambda: 0)
        for answer in answers:
            counter[answer] += 1
        tmp = []
        for an, cnt in counter.items():
            tmp.append((an, cnt))
        tmp.sort(key=lambda a : a[0])
        ans = 0
        for an, cnt in tmp:
            cnt_group = an + 1
            gcnt = (cnt - 1) // cnt_group + 1
            ans += gcnt * cnt_group
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.numRabbits([1, 1, 1]))