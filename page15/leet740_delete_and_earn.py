from typing import List
from collections import Counter


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = Counter(nums)
        keys = sorted(count.keys())
        mem = [[0,0] for _ in range(len(keys))]
        mem[0][0] = keys[0] * count[keys[0]]
        for i in range(1, len(keys)):
            cur_key = keys[i]
            last_key = keys[i - 1]
            if cur_key == last_key + 1:
                mem[i][0] = mem[i-1][1] + count[cur_key] * cur_key
            else:
                mem[i][0] = max(mem[i-1]) + count[cur_key] * cur_key
            mem[i][1] = max(mem[i-1])
        return max(mem[-1])


if __name__=="__main__":
    solution = Solution()
    print(solution.deleteAndEarn([2,2,3,3,4]))
