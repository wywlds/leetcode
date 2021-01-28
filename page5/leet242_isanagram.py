from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter1 = Counter(s)
        counter2 = Counter(s)
        for k, c in counter1:
            if k not in counter2:
                return False
            else:
                if counter2[k] != counter1[k]:
                    return False
        return len(counter2.keys()) == len(counter1.keys())