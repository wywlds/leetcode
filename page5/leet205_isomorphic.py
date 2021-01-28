class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dic1, dic2 = {}, {}
        for ch1, ch2 in zip(s, t):
            if ch1 in dic1 or ch2 in dic2:
                if ch1 in dic1 and ch2 in dic2 and dic1[ch1] == ch2 and dic2[ch2] == ch1:
                    continue
                else:
                    return False
            else:
                dic1[ch1] = ch2
                dic2[ch2] = ch1
        return True