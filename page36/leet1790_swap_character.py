class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        count = 0
        tup = None
        for ch1, ch2 in zip(s1, s2):
            if ch1 != ch2:
                if count == 0:
                    tup = [ch1, ch2]
                    count += 1
                elif count == 1:
                    if tup[1] != ch1 or tup[0] != ch2:
                        return False
                    count += 1
                else:
                    return False
        return True