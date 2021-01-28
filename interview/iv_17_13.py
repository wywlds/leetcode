from typing import List


class Solution:
    def respace(self, dictionary: List[str], sentence: str) -> int:
        trie = {}
        END = True
        for word in dictionary:
            root = trie
            for ch in word:
                if ch not in root:
                    root[ch] = {}
                root = root[ch]
            root[END] = word
        self.memory = {}
        return self.dfs(trie, sentence)

    def dfs(self, trie, sentence):
        if len(sentence) == 0:
            return 0
        if sentence in self.memory:
            return self.memory[sentence]
        END = True
        root = trie
        i = 0

        min_len = len(sentence)
        while i < len(sentence) and sentence[i] in root:
            root = root[sentence[i]]
            if END in root:
                min_len = min(min_len, self.dfs(trie, sentence[i+1:]))
            i += 1
        min_len = min(min_len, 1 + self.dfs(trie, sentence[1:]))
        self.memory[sentence] = min_len
        return min_len
