from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        LEN = 0
        mem = [[True] * LEN for _ in range(LEN)]
        for i in range(LEN-1, -1, -1):
            for j in range(i + 1, LEN):
                mem[i][j] = s[i] == s[j] and mem[i + 1][j - 1]
        res = []
        ans = []
        def dfs(i):
            if i == LEN:
                res.append(ans[:])
                return
            for j in range(i, LEN):
                if mem[i][j]:
                    ans.append(s[i: j + 1])
                    dfs(j + 1)
                    ans.pop()
        dfs(0)
        return res