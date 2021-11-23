from typing import List

from collections import defaultdict
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        vals = []
        for str in strs:
            c0 = 0
            c1 = 0
            for ch in str:
                if ch == '0':
                    c0 += 1
                else:
                    c1 += 1
            vals.append((c0, c1))
        memo = defaultdict(lambda: 0)
        memo[(0, 0)] = 0
        for i, (c0, c1) in enumerate(vals):
            for (l0, l1), cnt in list(memo.items()):
                n0, n1, ncnt = l0 + c0, l1 + c1, cnt + 1
                if n0 > m or n1 > n:
                    continue
                else:
                    memo[(n0, n1)] = max(ncnt, memo[(n0, n1)])
        return max(memo.values())


if __name__=="__main__":
    strs = ["0","1101","01","00111","1","10010","0","0","00","1","11","0011"]
    m = 63
    n = 36
    solution = Solution()
    print(solution.findMaxForm(strs, m, n))
