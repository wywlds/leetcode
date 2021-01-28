from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cont = Counter(s)
        for i, ch in enumerate(s):
            if cont[ch] == 1:
                return i
        return -1