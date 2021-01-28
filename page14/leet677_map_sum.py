class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        self.END = 0
        self.SUM = 1

    def insert(self, key: str, val: int) -> None:
        passes = [self.trie]
        cur = self.trie
        for ch in key:
            if ch not in cur:
                cur[ch] = {}
            cur = cur[ch]
            passes.append(cur)
        if self.END not in cur:
            cur[self.END] = 0
        last_value = cur[self.END]
        cur[self.END] = val
        delta = val - last_value
        for pas in passes:
            if self.SUM not in pas:
                pas[self.SUM] = val
            else:
                pas[self.SUM] += (val - delta)

    def sum(self, prefix: str) -> int:
        cur = self.trie
        for ch in prefix:
            if ch not in cur:
                return 0
            cur = cur[ch]
        return cur[self.SUM]
