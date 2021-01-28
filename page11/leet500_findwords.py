from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        line1 = "qwertyuiopQWERTYUIOP"
        line2 = "asdfghjklASDFGHJKL"
        line3 = "zxcvbnmZXCVBNM"
        pos = [0] * 128
        for albet in line1:
            pos[ord(albet)] = 1
        for albet in line2:
            pos[ord(albet)] = 2
        for albet in line3:
            pos[ord(albet)] = 3

        result = []
        for word in words:
            pos_w = pos[ord(word[0])]
            all_same_pos = True
            for albet in word[1:]:
                all_same_pos &= (pos[ord(albet)] == pos_w)
            if all_same_pos:
                result.append(word)
        return result