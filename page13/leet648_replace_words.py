from typing import List


class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        trie = {}
        END = True
        for root in dict:
            root_trie = trie
            for ch in root:
                if ch not in root_trie:
                    root_trie[ch] = {}
                root_trie = root_trie[ch]
            root_trie[END] = root
        new_words = []
        for word in sentence.split(" "):
            word_trie = trie
            added = False
            for ch in word:
                if ch in word_trie:
                    word_trie = word_trie[ch]
                    if END in word_trie:
                        new_words.append(word_trie[END])
                        added = True
                        break
                else:
                    break
            if not added:
                new_words.append(word)
        return " ".join(new_words)



