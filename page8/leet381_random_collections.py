import random

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []
        self.pos_dic = {}


    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.q.append(val)
        if val not in self.pos_dic:
            self.pos_dic[val] = set()
        self.pos_dic[val].add(len(self.q) - 1)
        return len(self.pos_dic[val]) == 1


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.pos_dic and len(self.pos_dic[val]) != 0:
            pos_set = self.pos_dic[val]
            pos = pos_set.pop()
            if pos != len(self.q) - 1:
                new_value = self.q[len(self.q) - 1]
                self.q[pos] = new_value
                self.pos_dic[new_value].remove(len(self.q) - 1)
                self.pos_dic[new_value].add(pos)
            self.q.pop()
            return True
        return False


    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if len(self.q) == 0:
            return None
        rand_pos = random.randint(0, len(self.q) - 1)
        return self.q[rand_pos]


if __name__=="__main__":
    random_col = RandomizedCollection()
    random_col.insert(1)
    random_col.insert(1)
    random_col.insert(1)
    random_col.insert(2)
    random_col.remove(1)
    for i in range(100):
        print(random_col.getRandom())