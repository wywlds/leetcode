from functools import lru_cache
from collections import Counter

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @lru_cache(None)
        def dfs(i1, i2, length):
            str1 = s1[i1:i1+length]
            str2 = s2[i2:i2+length]
            if str1 == str2:
                return True
            if Counter(str1) != Counter(str2):
                return False
            for sublen in range(1, length):
                if dfs(i1, i2, sublen) and dfs(i1 + sublen, i2 + sublen, length - sublen):
                    return True
                if dfs(i1, i2 + length - sublen, sublen) and dfs(i1 + sublen, i2, length-sublen):
                    return True
            return False

        return dfs(0, 0, len(s1))

def partition(li):
    pivot = li[0]
    l, r = 1, 1
    while r < len(li):
        if li[r] <= pivot:
            li[l], li[r] = li[r], li[l]
            l += 1
        r += 1
    li[l - 1], li[0] = pivot, li[l - 1]

if __name__=="__main__":
    # solution = Solution()
    # print(solution.isScramble("great", "rgeat"))
    from random import shuffle
    l = list(range(100))
    shuffle(l)
    print(l)
    partition(l)
    print(l)
