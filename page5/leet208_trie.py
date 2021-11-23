class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.data
        for ch in word:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur[0] = 0


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.data
        for ch in word:
            if ch not in cur:
                return False
            cur = cur[ch]
        return 0 in cur


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.data
        for ch in prefix:
            if ch not in cur:
                return False
            cur = cur[ch]
        return True

if __name__=="__main__":
    trie = Trie();
    trie.insert("apple");
    print(trie.search("apple"))   # 返回 True
    print(trie.search("app"))     # 返回 False
    print(trie.startsWith("app")) # 返回 True
    trie.insert("app");
    print(trie.search("app"))   # 返回 True