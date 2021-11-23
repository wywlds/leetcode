from typing import List

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        tree = {}
        for num in nums:
            cur = tree
            for i in range(31, -1, -1):
                cur_pos = (num >> i) & 1
                if cur_pos not in cur:
                    if i != 0:
                        cur[cur_pos] = {}
                        cur = cur[cur_pos]
                    else:
                        cur[cur_pos] = num
                else:
                    cur = cur[cur_pos]
        ans = 0
        for num in nums:
            cur = tree
            for i in range(31, -1, -1):
                cur_pos = (num >> i) & 1
                if cur_pos == 0:
                    cur_key = 1
                else:
                    cur_key = 0
                if cur_key in cur:
                    cur = cur[cur_key]
                else:
                    cur = cur[cur_pos]
            ans = max(ans, cur ^ num)
        return ans


if __name__=="__main__":
    solution = Solution()
    print(solution.findMaximumXOR([14,70,53,83,49,91,36,80,92,51,66,70]))