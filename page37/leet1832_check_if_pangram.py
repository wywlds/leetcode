class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        form = [0] * 26
        for i, ch in enumerate(sentence):
            form[ord(ch) - ord('a')] = 1
        return all([f == 1 for f in form])