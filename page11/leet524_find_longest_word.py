from typing import List


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def check(a, b):
            if len(a) > len(b):
                return False
            loc = -1
            for ch in a:
                loc = b.find(ch, loc + 1)
                if loc == -1:
                    return False
            return True

        d.sort(key=len, reverse=True)
        max_len = 0
        word_cands = []
        for word in d:
            len_word = len(word)
            if len_word < max_len:
                break
            if check(word, s):
                word_cands.append(word)
                max_len = len_word

        if word_cands:
            word_cands.sort()
            return word_cands[0]
        else:
            return ""
