class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = [None] * 10000


    def add(self, key: int) -> None:
        k = key % 10000
        if self.mem[k] is None:
            self.mem[k] = [key]
            return
        elif key not in self.mem[k]:
            self.mem[k].append(key)
        return

    def remove(self, key: int) -> None:
        if self.contains(key):
            self.mem[key % 10000].remove(key)

    def contains(self, key: int) -> bool:
        k = key % 10000
        if self.mem[k] is None:
            return False
        elif key not in self.mem[k]:
            return False
        return True