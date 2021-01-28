from typing import List


class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        def check(a, b):
            if len(a) > len(b):
                return False
            loc = -1
            for c in a:
                loc = b.find(c, loc + 1)
                if loc == -1:
                    return False
            return True
        strs.sort(key=len, reverse=True)
        for i, str in enumerate(strs):
            if all([not check(str, right_str) for j, right_str in enumerate(strs) if i != j]):
                return len(str)
        return -1


if __name__=="__main__":
    solution = Solution()
    print(solution.findLUSlength(["aaa", "aaa"]))
    print(solution.findLUSlength(["aaa", "aa"]))