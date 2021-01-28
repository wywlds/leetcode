from typing import List


class MagicDictionary:

    def __init__(self):
        self.magic_dict = {}
        self.END = 0

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            start_dict = self.magic_dict
            for ch in word:
                if ch not in start_dict:
                    start_dict[ch] = {}
                start_dict = start_dict[ch]
            start_dict[self.END] = word

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        start_dict = self.magic_dict
        for i, ch in enumerate(word):
            for next_c, next_trie in start_dict.items():
                sub_word = word[i+1:]
                if next_c != ch and self.exact_search(next_trie, sub_word):
                    return True
            if ch in start_dict:
                start_dict = start_dict[ch]
        return False

    def exact_search(self, trie, word) -> bool:
        for ch in word:
            if ch not in trie:
                return False
            trie = trie[ch]
        return self.END in trie



