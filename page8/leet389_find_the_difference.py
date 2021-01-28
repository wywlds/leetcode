from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count1 = Counter(s)
        count2 = Counter(t)
        for w, c in count2.items():
            if w not in count1 or count1.get(w) == c + 1:
                return w
        return None