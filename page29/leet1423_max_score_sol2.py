from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        mem = [[0] * (k + 1) for _ in range(k + 1)]
        ans = 0
        def dfs(l, r, base):
            mem[l][r] = 1
            nonlocal ans
            if l + r == k:
                ans = max(ans, base)
            else:
                if mem[l][r+1] == 0:
                    dfs(l, r + 1, base + cardPoints[-r-1])
                if mem[l+1][r] == 0:
                    dfs(l+1, r, base+cardPoints[l])
        dfs(0, 0, 0)
        return ans

if __name__=="__main__":
    solution = Solution()
    print(solution.maxScore([1,23,4,2,3,5,12,2], 3))