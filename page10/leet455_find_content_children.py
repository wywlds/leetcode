from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        s.append(0)
        i, j = 0, 0
        while i < len(g):
            if g[i] <= s[j]:
                i += 1
                j += 1
            else:
                i += 1
        return j

if __name__=="__main__":
    solution = Solution()
    print(solution.findContentChildren([10,9,8,7], [8,7,5,6]))
