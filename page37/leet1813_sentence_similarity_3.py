class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        if len(sentence1) < len(sentence2):
            return self.areSentencesSimilar(sentence2, sentence1)
        words1 = sentence1.split(" ")
        words2 = sentence2.split(" ")
        p1 = 0
        while p1 < len(words2) and p1 < len(words1):
            if words1[p1] != words2[p1]:
                break
            p1 += 1
        if p1 == len(words2):
            return True
        p2 = 0
        while p2 < len(words2) and p1 < len(words1):
            if words1[-p2 -1] != words2[-p2 -1]:
                break
            p2 += 1
        return p1 + p2 >= len(words2)