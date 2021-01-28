from collections import Counter
from typing import List


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        counts = [float('inf')] * 26
        for word in A:
            counter = Counter(word)
            for ind in range(26):
                letter = chr(ind + ord('a'))
                if letter in counter:
                    counts[ind] = min(counts[ind], counter[letter])
                else:
                    counts[ind] = 0
        ans = []
        for ind in range(26):
            count = counts[ind]
            if count > 0:
                letter = chr(ind + ord('a'))
                for i in range(count):
                    ans.append(letter)
        return ans