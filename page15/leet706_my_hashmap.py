class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = [None] * 10000


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        k = key % 10000
        if self.mem[k] is None:
            self.mem[k] = [[key, value]]
            return
        for tup in self.mem[k]:
            if tup[0] == key:
                tup[1] = value
                return
        self.mem[k].append([key, value])
        return



    def get(self, key: int) -> int:
        k = key % 10000
        if self.mem[k] is None:
            return -1
        for tup in self.mem[k]:
            if tup[0] == key:
                return tup[1]
        return -1

    def remove(self, key: int) -> None:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        k = key % 10000
        if self.mem[k] is None:
            return
        j = -1
        for i in range(len(self.mem[k])):
            if key == self.mem[k][0]:
                j = i
        if j != -1:
            self.mem[k].pop(j)

