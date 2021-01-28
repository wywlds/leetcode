from typing import List

import copy
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.ans = []
        self.dfs([], 0, n, k)
        return self.ans

    def dfs(self, base_nums, m, n, k):
        if m + k > n:
            return

        if k == 0:
            self.ans.append([base_num + 1 for base_num in base_nums])
            return

        for j in range(m, n):
            base_nums.append(j)
            self.dfs(base_nums, j + 1, n, k - 1)
            base_nums.pop()

if __name__=="__main__":
    solution = Solution()
    print(solution.combine(3, 2))
