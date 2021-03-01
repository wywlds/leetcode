from typing import List


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        ans = []
        for l in A:
            ans.append([~i & 1 for i in l[::-1]])
        return ans