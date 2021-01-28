class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        if pattern is None or s is None:
            return False
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        dic = {}
        word_set = set()
        for let, word in zip(pattern, words):
            if let not in dic and word not in word_set:
                dic[let] = word
                word_set.add(word)
            else:
                if let not in dic and word in word_set:
                    return False
                elif word != dic[let]:
                    return False
        return True